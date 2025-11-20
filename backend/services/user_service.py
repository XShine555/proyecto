from datetime import datetime, timezone
from sqlalchemy import func
from sqlmodel import Session, and_, select, or_

from entities.tipus_registre import TipusRegistreEnum
from entities.classe import Classe
from entities.dispositiu import Dispositiu
from entities.horari import Horari
from entities.usuari import Usuari
from entities.usuari_classe import UsuariClasse
from entities.assistencia import Assistencia

class UserService:
    def __init__(self, session_factory, assistance_service, logger):
        self.__session_factory = session_factory
        self.__assistance_service = assistance_service
        self.__logger = logger

    def get_user_by_id(self, user_id) -> Usuari | None:
        with self.__session_factory() as session:
            return session.exec(select(Usuari).where(Usuari.id == user_id)).first()
    
    def get_user_by_rfid_id(self, rfid_id) -> Usuari | None:
        with self.__session_factory() as session:
            return session.exec(select(Usuari).where(Usuari.targeta_rfid == rfid_id)).first()

    def has_access(self, user: Usuari, dispositiu: Dispositiu) -> bool:
        session: Session = self.__session_factory()
        try:
            classe: Classe = dispositiu.classe
            if not classe:
                self.__logger.info(f"Access denied: Device {dispositiu.id} has no associated class.")
                return False

            usuari_classe = session.exec(
                select(UsuariClasse).where(
                    UsuariClasse.usuari_id == user.id,
                    UsuariClasse.classe_id == classe.id
                )
            ).first()

            if not usuari_classe:
                self.__logger.info(f"Access denied: User {user.id} has no permission for class {classe.id}.")
                return False
            
            horari = session.exec(
                select(Horari).where(
                    Horari.classe_id == classe.id,
                    Horari.timestamp_inici <= datetime.now(),
                    Horari.timestamp_fi >= datetime.now()
                )
            ).first()

            if not horari:
                self.__logger.info(f"Access denied: No active schedule for class {classe.id}.")
                return False
            
            self.__logger.info(f"Access granted: User {user.id} to device {dispositiu.id}.")
            return True
        finally:
            session.close()

    def has_absence(self, user: Usuari, clase: Classe, horari: Horari) -> bool:
        session: Session = self.__session_factory()
        try:
            absence = session.exec(
                select(func.count()).where(
                    Usuari.id == user.id,
                    Usuari.assistencies.any(
                        and_(
                            Assistencia.classe_id == clase.id,
                            Assistencia.horari_id == horari.id,
                            Assistencia.tipus_registre == TipusRegistreEnum.no_assistit
                        )
                    )
                )
            ).one()

            return absence > 0
        finally:
            session.close()

    def has_assisted(self, user: Usuari, clase: Classe, horari: Horari) -> bool:
        session: Session = self.__session_factory()
        try:
            assistencia = session.exec(
                select(func.count()).where(
                    Usuari.id == user.id,
                    Usuari.assistencies.any(
                        and_(
                            Assistencia.classe_id == clase.id,
                            Assistencia.horari_id == horari.id,
                            or_(
                                Assistencia.tipus_registre == TipusRegistreEnum.assistit,
                                Assistencia.tipus_registre == TipusRegistreEnum.retard
                            )
                        )
                    )
                )
            ).one()

            return assistencia > 0
        finally:
            session.close()

    def mark_assistance(self, user: Usuari, classe: Classe, horari: Horari) -> None:
        session: Session = self.__session_factory()

        try:
            assistance = None

            if self.has_absence(user, classe, horari):
                assistance = self.__assistance_service.get_assistance_by_user_id(user.id)
                assistance.tipus_registre = TipusRegistreEnum.retard
            else:
                assistance = Assistencia(
                    usuari_id=user.id,
                    timestamp_assistencia=lambda: datetime.now(),
                    horari_id=horari.id,
                    classe_id=classe.id,
                    tipus_registre=TipusRegistreEnum.assistit
                )
            session.add(assistance)
            session.commit()
            session.refresh(assistance)
            self.__logger.info(f"Assistance recorded for user {user.id}.")
        finally:
            session.close()