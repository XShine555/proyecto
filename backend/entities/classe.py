from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Relationship, SQLModel, Field

if TYPE_CHECKING:
    from entities.dispositiu import Dispositiu

class Classe(SQLModel, table=True):
    __tablename__ = "CLASSES"

    id: Optional[int] = Field(default=None, primary_key=True)
    nom: str = Field(max_length=100)
    planta: int

    dispositius: List["Dispositiu"] = Relationship(back_populates="classe")