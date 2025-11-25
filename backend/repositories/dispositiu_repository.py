from sqlmodel import select
from entities.dispositiu import Dispositiu
from sqlalchemy.orm import selectinload

class DispositiuRepository:
    def __init__(self, session_factory):
        self.__session_factory = session_factory

    def get_dispositiu_by_id(self, id: int) -> Dispositiu | None:
        with self.__session_factory() as session:
            return session.exec(
                select(Dispositiu)
                .options(selectinload(Dispositiu.classe))
                .where(Dispositiu.id == id)
            ).first()
        
    def get_dispositiu_by_device_id(self, dispositiu_id: str) -> Dispositiu | None:
        with self.__session_factory() as session:
            return session.exec(
                select(Dispositiu)
                .options(selectinload(Dispositiu.classe))
                .where(Dispositiu.device_id == dispositiu_id)
            ).first()
        
    def get_dispositiu_by_classe_id(self, classe_id: int) -> Dispositiu | None:
        with self.__session_factory() as session:
            return session.exec(
                select(Dispositiu)
                .options(selectinload(Dispositiu.classe))
                .where(Dispositiu.classe_id == classe_id)
            ).first()