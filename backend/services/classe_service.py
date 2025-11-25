from datetime import datetime
from services.horari_service import HorariService
from entities.assignatura import Assignatura
from repositories.classe_repository import ClasseRepository
from services.assignatura_service import AssignaturaService

class ClasseService:
    def __init__(self, 
                 classe_repository: ClasseRepository, 
                 assignatura_service: AssignaturaService, 
                 horari_service: HorariService,
                 logger):
        self.__classe_repository = classe_repository
        self.__assignatura_service = assignatura_service
        self.__horari_service = horari_service
        self.__logger = logger

    def get_classe_by_id(self, id: int):
        return self.__classe_repository.get_classe_by_id(id)
    
    def get_active_assignatura_for_classe(self, classe_id: int) -> Assignatura | None:
        classe = self.get_classe_by_id(classe_id)
        if not classe:
            self.__logger.error(f"Classe with ID {classe_id} not found.")
            return None
        
        assignatures = self.__assignatura_service.get_assignatura_by_classe_id(classe.id)
        if not assignatures or len(assignatures) == 0:
            self.__logger.error(f"No assignatures found for Classe ID {classe.id}.")
            return None
        
        for assignatura in assignatures:
            active_horari = self.__horari_service.get_active_horari(assignatura.id)
            if active_horari:
                return assignatura

        return None