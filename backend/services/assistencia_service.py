from datetime import datetime
from entities.horari import Horari
from services.horari_service import HorariService
from entities.tipus_registre import TipusRegistreEnum
from entities.assistencia import Assistencia
from repositories.assistencia_repository import AssistenciaRepository

class AssistenciaService:
    def __init__(self, 
                 assistencia_repository: AssistenciaRepository, 
                 horari_service: HorariService,
                 logger):
        self.__assistencia_repository: AssistenciaRepository = assistencia_repository
        self.__horari_service: HorariService = horari_service
        self.__logger = logger

    def get_assistencia_by_user_id(self, user_id: int, assignatura_id: int, horari_id: int) -> Assistencia | None:
        return self.__assistencia_repository.get_assistencia_by_user_id(user_id, assignatura_id, horari_id)
        
    def get_all_assistencias_by_user_id(self, user_id: int) -> list[Assistencia]:
        return self.__assistencia_repository.get_all_assistencias_by_user_id(user_id)
    
    def get_all_assistencias_by_user_id_and_classe_id(self, user_id: int, assignatura_id: int) -> list[Assistencia]:
        return self.__assistencia_repository.get_all_assistencias_by_user_id_and_classe_id(user_id, assignatura_id)
    
    def get_all_assistencias_by_user_id_and_horari_id(self, user_id: int, horari_id: int) -> list[Assistencia]:
        return self.__assistencia_repository.get_all_assistencias_by_user_id_and_horari_id(user_id, horari_id)
    
    def has_assistencia(self, user_id: int, assignatura_id: int, horari_id: int) -> bool:
        assistencia = self.get_assistencia_by_user_id(user_id, assignatura_id, horari_id)
        return assistencia is not None and (assistencia.tipus_registre == TipusRegistreEnum.assistit or assistencia.tipus_registre == TipusRegistreEnum.sortida)

    def mark_assistencia(self, user_id: int, assignatura_id: int, horari_id: int):
        get_horari: Horari | None = self.__horari_service.get_horari_by_id(horari_id)
        if not get_horari:
            self.__logger.error(f"Horari with ID {horari_id} not found.")
            return
        
        existing_assistencia = self.get_assistencia_by_user_id(user_id, assignatura_id, horari_id)
        now = datetime.now()
        
        if existing_assistencia:
            if existing_assistencia.tipus_registre == TipusRegistreEnum.assistit:
                return
            
            existing_assistencia.tipus_registre = TipusRegistreEnum.retard
            existing_assistencia.timestamp = now
            self.__assistencia_repository.add_assistencia(existing_assistencia)
        else:
            is_late = get_horari.timestamp_inici < now and now > get_horari.timestamp_fi
            tipus_registre = TipusRegistreEnum.retard if is_late else TipusRegistreEnum.assistit
            
            new_assistencia = Assistencia(
                usuari_id=user_id,
                assignatura_id=assignatura_id,
                horari_id=horari_id,
                tipus_registre=tipus_registre,
                timestamp=now
            )
            self.__assistencia_repository.add_assistencia(new_assistencia)
            
        return