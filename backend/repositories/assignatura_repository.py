from sqlmodel import select
from entities.usuari_assignatures import UsuariAssignatura
from entities.assignatura import Assignatura

class AssignaturaRepository:
    def __init__(self, session_factory):
        self.__session_factory = session_factory

    def get_all_assignatures(self) -> list[Assignatura]:
        with self.__session_factory() as session:
            return session.exec(
                select(Assignatura)
            ).all()

    def get_assignatura_by_id(self, id: int) -> Assignatura | None:
        with self.__session_factory() as session:
            return session.exec(
                select(Assignatura).where(Assignatura.id == id)
            ).first()
        
    def get_assignatura_by_classe_id(self, classe_id: int) -> list[Assignatura]:
        with self.__session_factory() as session:
            return session.exec(
                select(Assignatura).where(Assignatura.classe_id == classe_id)
            ).all()
            
    def has_user_access(self, usuari, assignatura_id: int) -> bool:
        with self.__session_factory() as session:
            result = session.exec(
                select(UsuariAssignatura).where(
                    UsuariAssignatura.usuari_id == usuari.id,
                    UsuariAssignatura.assignatura_id == assignatura_id
                )
            ).first()
            return result is not None