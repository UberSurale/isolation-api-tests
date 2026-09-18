import time

from tests.clients.kafka.producer import KafkaProducerTestClient
from tests.schemas.operations import OperationEventTestSchema
from tests.tools import allure

from tests.config import test_settings
from tests.tools.logger import get_test_logger
from tests.types.operations import OperationTestStatus, OperationTestType


class OperationsKafkaProducerTestClient(KafkaProducerTestClient):

    @allure.step("Produce operation event")
    def produce_operation_event_api(
        self,
        event: OperationEventTestSchema,
    ) -> OperationEventTestSchema:
        self.produce(
            topic="operations-service.operation-even.inbox",
            value=event.model_dump_json()
        )
        self.flush_all()
        time.sleep(test_settings.operations_processing_wait_timeout)


    @allure.step("Produce in progress purchase operation event")
    def produce_in_progress_purchase_operation_event(self) -> OperationEventTestSchema:
        return self.produce_operation_event_api(
            OperationEventTestSchema(
                type=OperationTestType.PURCHASE,
                status=OperationTestStatus.IN_PROGRESS,
            )
        )


    @allure.step("Produce completed purchase operation event")
    def produce_completed_purchase_operation_event(self) -> OperationEventTestSchema:
        return self.produce_operation_event_api(
            OperationEventTestSchema(
                type=OperationTestType.PURCHASE,
                status=OperationTestStatus.COMPLETED,
            )
        )


def build_operations_kafka_producer_test_client() -> OperationsKafkaProducerTestClient:
    return OperationsKafkaProducerTestClient(
        config=test_settings.operations_kafka_client,
        logger=get_test_logger("OPERATIONS_KAFKA_PRODUCER_TEST_CLIENT"),
    )

    