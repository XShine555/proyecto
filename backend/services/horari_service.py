from datetime import datetime
from repositories.horari_repository import HorariRepository
from entities.horari import Horari

class HorariService:
    def __init__(self, horari_repository, logger):
        self.__horari_repository: HorariRepository = horari_repository
        self.__logger = logger

    def get_horari_by_id(self, id: int) -> Horari | None:
        return self.__horari_repository.get_horari_by_id(id)

    def get_active_horari(self, assignatura_id: int) -> Horari | None:
        timestamp = datetime.now()
        return self.__horari_repository.get_horari_by_assignatura_and_current_time(assignatura_id, timestamp)
            