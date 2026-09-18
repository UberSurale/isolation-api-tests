from tests.clients.postgres.operations.model import OperationsTestModel
from tests.clients.postgres.repository import PostgresTestRepository
from tests.tools import allure
from tests.tools.fakers import fake
from tests.types.operations import OperationTestStatus, OperationTestType
from tests.clients.postgres.operations.session import operations_test_session_factory


class OperationsPostgresTestRepository(PostgresTestRepository):
    @allure.step("Create in progress purchase operation")
    def create_in_progress_purchase_operation(self) -> OperationsTestModel:
        return self.create(
            OperationsTestModel(
                # UUID генерируем детерминированно (в рамках fake),
                # чтобы тест мог опираться на конкретные значения.
                id=fake.uuid(),

                # Тип и статус задаём явно, потому что это часть сценария.
                type=OperationTestType.PURCHASE,
                status=OperationTestStatus.IN_PROGRESS,

                # Остальные поля — реалистичные значения,
                # которые не важны для логики фильтрации,
                # но важны для "живых" данных в тестовом слое.
                amount=fake.amount(),
                user_id=fake.uuid(),
                card_id=fake.uuid(),
                category=fake.category(),
                account_id=fake.uuid(),
                created_at=fake.date_time(),
            )
        )


    @allure.step("Create completed purchase operation")
    def create_completed_purchase_operation(self) -> OperationsTestModel:
        return self.create(
            OperationsTestModel(
                id=fake.uuid(),
                type=OperationTestType.PURCHASE,
                status=OperationTestStatus.COMPLETED,
                amount=fake.amount(),
                user_id=fake.uuid(),
                card_id=fake.uuid(),
                category=fake.category(),
                account_id=fake.uuid(),
                created_at=fake.date_time(),
            )
        )


def get_operation_postgres_test_repository() -> OperationsPostgresTestRepository:
    return OperationsPostgresTestRepository(
        session_factory=operations_test_session_factory
    )