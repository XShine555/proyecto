from datetime import datetime
from sqlmodel import select
from entities.horari import Horari

class HorariService:
    def __init__(self, session_factory, user_service, device_service, logger):
        self.__session_factory = session_factory
        self.__logger = logger

    def get_active_horari_for_classe(self, classe_id: int, timestamp: datetime) -> Horari | None:
        try:
            session = self.__session_factory()

            result = session.exec(
                select(Horari).where(
                    Horari.classe_id == classe_id,
                    Horari.timestamp_inici <= timestamp,
                    Horari.timestamp_fi >= timestamp
                )
            )
            return result.first()
        finally:
            session.close()
        
    def is_horari_active(self, horari: Horari, timestamp: datetime) -> bool:
        return horari.timestamp_inici <= timestamp <= horari.timestamp_fi
            