
from contextlib import contextmanager
from typing import Generator, TypeVar

from sqlalchemy.orm import Session, sessionmaker

from tests.clients.postgres.base import BaseTestModel


ModelT = TypeVar("ModelT", bound=BaseTestModel)

class PostgresTestRepository:
    def __init__(self, session_factory: sessionmaker[Session]) -> None:
        self.session_factory = session_factory


    @contextmanager
    def session_read(self) -> Generator[Session, None, None]:
        session = self.session_factory()
        try:
            yield session
        finally:
            session.close()


    def create(self, instance: ModelT) -> ModelT:
        with self.session_write() as session:
            session.add(instance)
            session.flush()
            session.refresh(instance)

        return instance