from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.usuari import Usuari

class Alerta(SQLModel, table=True):
    __tablename__ = "ALERTES"

    id: Optional[int] = Field(default=None, primary_key=True)
    usuari_id: int = Field(foreign_key="USUARIS.id")
    tipus: str
    percentatge_faltes: Optional[float] = None
    notificat: bool = Field(default=False)

    usuari: "Usuari" = Relationship(back_populates="alertes")