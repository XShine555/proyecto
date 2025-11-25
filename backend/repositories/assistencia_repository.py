from sqlmodel import select
from entities.assistencia import Assistencia

class AssistenciaRepository:
    def __init__(self, session_factory):
        self.__session_factory = session_factory

    def get_assistencia_by_user_id(self, user_id: int, assignatura_id: int, horari_id: int) -> Assistencia | None:
        with self.__session_factory() as session:
            return session.exec(
                select(Assistencia).where(Assistencia.usuari_id == user_id, Assistencia.assignatura_id == assignatura_id, Assistencia.horari_id == horari_id)
            ).first()
        
    def get_all_assistencias_by_user_id(self, user_id: int) -> list[Assistencia]:
        with self.__session_factory() as session:
            return session.exec(
                select(Assistencia).where(Assistencia.usuari_id == user_id)
            ).all()
        
    def get_all_assistencias_by_user_id_and_assignatura_id(self, user_id: int, assignatura_id: int) -> list[Assistencia]:
        with self.__session_factory() as session:
            return session.exec(
                select(Assistencia).where(Assistencia.usuari_id == user_id, Assistencia.assignatura_id == assignatura_id)
            ).all()
        
    def get_all_assistencias_by_user_id_and_horari_id(self, user_id: int, horari_id: int) -> list[Assistencia]:
        with self.__session_factory() as session:
            return session.exec(
                select(Assistencia).where(Assistencia.usuari_id == user_id, Assistencia.horari_id == horari_id)
            ).all()
        
    def add_assistencia(self, assistencia: Assistencia) -> Assistencia:
        with self.__session_factory() as session:
            session.add(assistencia)
            session.commit()
            session.refresh(assistencia)
            return assistencia
        
    def delete_assistencia(self, assistencia: Assistencia) -> None:
        with self.__session_factory() as session:
            session.delete(assistencia)
            session.commit()