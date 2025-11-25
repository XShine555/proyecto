from services.horari_service import HorariService
from repositories.usuari_repository import UsuariRepository
from services.assignatura_service import AssignaturaService

class UsuariService:
    def __init__(self, usuari_repository: UsuariRepository, assignatura_service: AssignaturaService, logger):
        self.__usuari_repository = usuari_repository
        self.__assignatura_service = assignatura_service
        self.__logger = logger

    def get_usuari_by_id(self, id: int):
        return self.__usuari_repository.get_usuari_by_id(id)
    
    def get_usuari_by_rfid(self, rfid: str):
        return self.__usuari_repository.get_usuari_by_rfid(rfid)
    
    def has_usuari_access_to_assignatura(self, usuari_id: int, assignatura_id: int) -> bool:
        usuari = self.get_usuari_by_id(usuari_id)
        if not usuari:
            self.__logger.warning(f"Usuari with ID {usuari_id} not found.")
            return False
        
        for usuari_assignatura in usuari.usuari_assignatures:
            if usuari_assignatura.assignatura_id == assignatura_id:
                return True
  
        return False