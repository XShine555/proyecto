from typing import List
from entities.assignatura import Assignatura
from repositories.assignatura_repository import AssignaturaRepository

class AssignaturaService:
    def __init__(self, assignatura_repository: AssignaturaRepository, logger):
        self.__assignatura_repository = assignatura_repository
        self.__logger = logger

    def get_assignatura_by_id(self, id: int) -> Assignatura | None:
        return self.__assignatura_repository.get_assignatura_by_id(id)
    
    def get_assignatura_by_classe_id(self, classe_id: int) -> List[Assignatura]:
        return self.__assignatura_repository.get_assignatura_by_classe_id(classe_id)
    
    def get_all_assignatures(self) -> List[Assignatura]:
        return self.__assignatura_repository.get_all_assignatures()
    
    def has_user_access(self, usuari, assignatura_id: int) -> bool:
        for usuari_assignatura in usuari.usuari_assignatures:
            if usuari_assignatura.assignatura_id == assignatura_id:
                return True
        return False