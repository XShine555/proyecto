from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
     from entities.classe import Classe
     from entities.usuari import Usuari

class UsuariClasse(SQLModel, table=True):
    __tablename__ = "USUARIS_CLASSES"

    usuari_id: int = Field(foreign_key="USUARIS.id", primary_key=True)
    classe_id: int = Field(foreign_key="CLASSES.id", primary_key=True)

    usuari: "Usuari" = Relationship(back_populates="usuaris_classes")
    classe: "Classe" = Relationship(back_populates="usuaris")

from entities.classe import Classe
from entities.usuari import Usuari