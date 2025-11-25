from sqlmodel import select
from entities.usuari import Usuari
from entities.usuari_assignatures import UsuariAssignatura
from sqlalchemy.orm import selectinload

class UsuariRepository:
    def __init__(self, session_factory):
        self.__session_factory = session_factory

    def get_usuari_by_id(self, id: int) -> Usuari | None:
        with self.__session_factory() as session:
            return session.exec(
                select(Usuari)
                .options(selectinload(Usuari.usuari_assignatures).selectinload(UsuariAssignatura.assignatura))
                .where(Usuari.id == id)
            ).first()
        
    def get_usuari_by_rfid(self, rfid: str) -> Usuari | None:
        with self.__session_factory() as session:
            return session.exec(
                select(Usuari)
                .options(selectinload(Usuari.usuari_assignatures).selectinload(UsuariAssignatura.assignatura))
                .where(Usuari.targeta_rfid == rfid)
            ).first()