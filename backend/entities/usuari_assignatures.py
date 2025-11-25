from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
     from entities.assignatura import Assignatura
     from entities.usuari import Usuari

class UsuariAssignatura(SQLModel, table=True):
    __tablename__ = "USUARIS_ASSIGNATURES"

    usuari_id: int = Field(foreign_key="USUARIS.id", primary_key=True)
    assignatura_id: int = Field(foreign_key="ASSIGNATURES.id", primary_key=True)

    usuari: "Usuari" = Relationship(back_populates="usuari_assignatures")
    assignatura: "Assignatura" = Relationship(back_populates="assignatura_usuaris")

from entities.assignatura import Assignatura
from entities.usuari import Usuari