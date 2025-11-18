from datetime import datetime, timezone
from sqlalchemy import func
from sqlmodel import Session, and_, select

from entities.tipus_registre import TipusRegistreEnum
from entities.classe import Classe
from entities.dispositiu import Dispositiu
from entities.horari import Horari
from entities.usuari import Usuari
from entities.usuari_classe import UsuariClasse
from entities.assistencia import Assistencia

class DeviceService:
    def __init__(self, session_factory, logger):
        self.__session_factory = session_factory
        self.__logger = logger

    def get_device_by_id(self, device_id) -> Dispositiu | None:
        with self.__session_factory() as session:
            return session.exec(select(Dispositiu).where(Dispositiu.device_id == device_id)).first()