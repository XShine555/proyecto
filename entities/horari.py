from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.assistencia import Assistencia
    from entities.classe import Classe

class Horari(SQLModel, table=True):
    __tablename__ = "HORARIS"

    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp_inici: datetime
    timestamp_fi: datetime
    classe_id: int = Field(foreign_key="CLASSES.id")

    classe: "Classe" = Relationship(back_populates="horaris")
    assistencies: List["Assistencia"] = Relationship(back_populates="horari")

from entities.assistencia import Assistencia
from entities.classe import Classe