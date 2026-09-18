import uuid

from sqlalchemy import UUID, Column, String
from sqlalchemy.orm import Mapped

from tests.clients.postgres.base import BaseTestModel


class OperationsTestModel(BaseTestModel):

    __tablename__ = "operations"

    id: Mapped[uuid.UUID] = Column(UUID, nullable=False, primary_key=True)

    type: Mapped[str] = Column(String(length=50), nullable=False)

    status: Mapped[str] = Column(String(length=50), nullable=False)

    # amount — сумма операции.
    amount: Mapped[float] = Column(Float, nullable=False)

    # user_id / card_id / account_id — связи с сущностями внешнего домена.
    # В рамках тестового слоя это просто UUID-идентификаторы,
    # достаточные для фильтрации и проверки.
    user_id: Mapped[uuid.UUID] = Column(UUID, nullable=False)
    card_id: Mapped[uuid.UUID] = Column(UUID, nullable=False)
    account_id: Mapped[uuid.UUID] = Column(UUID, nullable=False)

    # category — бизнес-атрибут операции (например, merchant category).
    category: Mapped[str] = Column(String(length=50), nullable=False)

    # created_at — время создания операции.
    # В тестах это поле часто нужно, чтобы проверять сортировки
    # или просто иметь реалистичные данные.
    created_at: Mapped[datetime] = Column(DateTime, nullable=False)

                  
