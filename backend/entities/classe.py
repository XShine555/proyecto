from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.dispositiu import Dispositiu
    from entities.horari import Horari
    from entities.usuari_classe import UsuariClasse
    from entities.assistencia import Assistencia

class Classe(SQLModel, table=True):
    __tablename__ = "CLASSES"

    id: Optional[int] = Field(default=None, primary_key=True)
    nom: str
    planta: Optional[int] = None

    dispositius: List["Dispositiu"] = Relationship(back_populates="classe")
    horaris: List["Horari"] = Relationship(back_populates="classe")
    usuaris: List["UsuariClasse"] = Relationship(back_populates="classe")
    assistencies: List["Assistencia"] = Relationship(back_populates="classe")

from entities.assistencia import Assistencia
from entities.dispositiu import Dispositiu
from entities.horari import Horari
from entities.usuari_classe import UsuariClasse