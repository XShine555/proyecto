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
user_logger = logging.getLogger("user_service")

from services.mqtt_service import MQTTService
from services.user_service import UserService
from services.device_service import DeviceService
user_service = UserService(session_factory, user_logger)
device_service = DeviceService(session_factory, device_logger)
mqtt_service = MQTTService(session_factory, user_service, device_service, mqtt_logger)

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