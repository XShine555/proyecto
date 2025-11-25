from sqlmodel import select
from entities.classe import Classe

class ClasseRepository:
    def __init__(self, session_factory):
        self.__session_factory = session_factory

    def get_classe_by_id(self, id: int) -> Classe | None:
        with self.__session_factory() as session:
            return session.exec(
                select(Classe).where(Classe.id == id)
            ).first()