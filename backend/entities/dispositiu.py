from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from entities.classe import Classe

class Dispositiu(SQLModel, table=True):
    __tablename__ = "DISPOSITIUS"

    id: Optional[int] = Field(default=None, primary_key=True)
    device_id: str = Field(unique=True)
    actiu: bool = Field(default=True)
    classe_id: int = Field(foreign_key="CLASSES.id")

    classe: "Classe" = Relationship(back_populates="dispositius")

from entities.classe import Classe