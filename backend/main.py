from dotenv import load_dotenv

load_dotenv()

from db.dbcontext import init_db, get_session

init_db()

import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager

def session_factory():
    return next(get_session())

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

mqtt_logger = logging.getLogger("mqtt_service")
device_logger = logging.getLogger("device_service")
horari_logger = logging.getLogger("horari_service")
user_logger = logging.getLogger("user_service")
assistencia_logger = logging.getLogger("assistencia_service")
assignatura_logger = logging.getLogger("assignatura_service")
classe_logger = logging.getLogger("classe_service")

from repositories.classe_repository import ClasseRepository
from repositories.assignatura_repository import AssignaturaRepository
from repositories.usuari_repository import UsuariRepository
from repositories.dispositiu_repository import DispositiuRepository
from repositories.horari_repository import HorariRepository
from repositories.assistencia_repository import AssistenciaRepository

classe_repository = ClasseRepository(session_factory)
assignatura_repository = AssignaturaRepository(session_factory)
usuari_repository = UsuariRepository(session_factory)
dispositiu_repository = DispositiuRepository(session_factory)
horari_repository = HorariRepository(session_factory)
assistencia_repository = AssistenciaRepository(session_factory)

from services.mqtt_service import MQTTService
from services.usuari_service import UsuariService
from services.dispositiu_service import DispositiuService
from services.horari_service import HorariService
from services.assistencia_service import AssistenciaService
from services.assignatura_service import AssignaturaService
from services.classe_service import ClasseService

assignatura_service = AssignaturaService(assignatura_repository, assignatura_logger)
horari_service = HorariService(horari_repository, horari_logger)
classe_service = ClasseService(classe_repository, assignatura_service, horari_service, classe_logger)
assistencia_service = AssistenciaService(assistencia_repository, horari_service, assistencia_logger)
user_service = UsuariService(usuari_repository, assignatura_service, user_logger)
dispositiu_service = DispositiuService(dispositiu_repository, device_logger)
mqtt_service = MQTTService(session_factory, user_service, dispositiu_service, classe_service, assistencia_service, horari_service, mqtt_logger)

@asynccontextmanager
async def lifespan(app):
    mqtt_service.connect()
    try:
        yield
    finally:
        mqtt_service.disconnect()

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def get_health():
    return {"status": "ok"}