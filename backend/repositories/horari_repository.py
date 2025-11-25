from datetime import datetime
from sqlmodel import select
from entities.horari import Horari

class HorariRepository:
    def __init__(self, session_factory):
        self.__session_factory = session_factory

    def get_horari_by_id(self, id: int) -> Horari | None:
        with self.__session_factory() as session:
            return session.exec(
                select(Horari).where(Horari.id == id)
            ).first()
        
    def get_horari_by_assignatura_id(self, assignatura_id: int) -> list[Horari]:
        with self.__session_factory() as session:
            return session.exec(
                select(Horari).where(Horari.assignatura_id == assignatura_id)
            ).all()
        
    def get_horari_by_assignatura_and_current_time(self, assignatura_id: int, timestamp: datetime) -> Horari | None:
        with self.__session_factory() as session:
            return session.exec(
                select(Horari).where(
                    Horari.assignatura_id == assignatura_id,
                    Horari.timestamp_inici <= timestamp,
                    Horari.timestamp_fi >= timestamp
                )
            ).first()