from repositories.dispositiu_repository import DispositiuRepository

class DispositiuService:
    def __init__(self, dispositiu_repository: DispositiuRepository, logger):
        self.__dispositiu_repository = dispositiu_repository
        self.__logger = logger

    def get_dispositiu_by_id(self, id: int):
        return self.__dispositiu_repository.get_dispositiu_by_id(id)
    
    def get_dispositiu_by_device_id(self, dispositiu_id: int):
        return self.__dispositiu_repository.get_dispositiu_by_device_id(dispositiu_id)
    
    def get_dispositiu_by_classe_id(self, classe_id: int):
        return self.__dispositiu_repository.get_dispositiu_by_classe_id(classe_id)