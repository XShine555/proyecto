from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Relationship, SQLModel, Field

from entities.usuari_assignatures import UsuariAssignatura
from entities.tipus_usuari import TipusUsuariEnum

if TYPE_CHECKING:
    from entities.assistencia import Assistencia

class Usuari(SQLModel, table=True):
    __tablename__ = "USUARIS"

    id: Optional[int] = Field(default=None, primary_key=True)
    nom: str
    cognoms: str
    tipus: TipusUsuariEnum
    targeta_rfid: Optional[str] = Field(default=None, unique=True)
    actiu: bool = Field(default=True)

    assistencies: List["Assistencia"] = Relationship(back_populates="usuari")
    usuari_assignatures: List["UsuariAssignatura"] = Relationship(back_populates="usuari")