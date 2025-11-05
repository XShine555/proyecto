from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.dispositiu import Dispositiu
    from entities.horari import Horari
    from entities.permis_clase import PermisClasse

class Classe(SQLModel, table=True):
    __tablename__ = "CLASSES"

    id: Optional[int] = Field(default=None, primary_key=True)
    nom: str
    planta: Optional[int] = None

    dispositius: List["Dispositiu"] = Relationship(back_populates="classe")
    horaris: List["Horari"] = Relationship(back_populates="classe")
    permisos: List["PermisClasse"] = Relationship(back_populates="classe")

from entities.dispositiu import Dispositiu
from entities.horari import Horari
from entities.permis_clase import PermisClasse