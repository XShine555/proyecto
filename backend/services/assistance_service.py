from datetime import datetime, timezone
from sqlalchemy import func
from sqlmodel import Session, and_, select

from entities.tipus_registre import TipusRegistreEnum
from entities.classe import Classe
from entities.dispositiu import Dispositiu
from entities.horari import Horari
from entities.usuari import Usuari
from entities.usuari_classe import UsuariClasse
from entities.assistencia import Assistencia

class AssistanceService:
    def __init__(self, session_factory, logger):
        self.__session_factory = session_factory
        self.__logger = logger

    def get_assistance_by_user_id(self, user_id: int):
        session = self.__session_factory()
        try:
            result = session.exec(
                select(Assistencia).where(Assistencia.usuari_id == user_id)
            ).first()

            return result
        finally:
            session.close()