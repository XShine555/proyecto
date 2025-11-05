from enum import Enum

class TipusUsuariEnum(str, Enum):
    alumne = "alumne"
    professor = "professor"
    admin = "admin"