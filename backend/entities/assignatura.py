from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from entities.horari import Horari
    from entities.usuari_assignatures import UsuariAssignatura
    from entities.assistencia import Assistencia

class Assignatura(SQLModel, table=True):
    __tablename__ = "ASSIGNATURES"

    id: Optional[int] = Field(default=None, primary_key=True)
    nom: str
    classe_id: int = Field(foreign_key="CLASSES.id")

    horaris: List["Horari"] = Relationship(back_populates="assignatura")
    assignatura_usuaris: List["UsuariAssignatura"] = Relationship(back_populates="assignatura")
    assistencies: List["Assistencia"] = Relationship(back_populates="assignatura")