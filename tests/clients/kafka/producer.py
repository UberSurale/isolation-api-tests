import logging

from tests.tools import allure
from tests.tools.config.kafka import KafkaClientTestConfig
from confluent_kafka import Producer


class KafkaProducerTestClient:
    def __init__(
            self,
            config: KafkaClientTestConfig,
            logger: logging.Logger
    ):
        self.logger = logger
        self.producer = Producer(
            {
                "bootstrap.servers": config.bootstrap_servers,
            }
        )


    @allure.step("Produce message to topic {topic}")
    def produce(self, topic: str, value: str | bytes):
        try:
            self.producer.produce(topic, value)
            self.producer.poll(0)
            self.logger.info(f"Kafka message produced {topic}")
        except Exception as error:
            self.logger.exception(f"Kafka produce failed ${topic}:{error}")


    @allure.step('Flush all mesages')
    def flush_all(self, timeout: float = 10.0):
        self.logger.info("Kafka producer flush stated")
        self.producer.flush(timeout)
        self.logger.info("Kafka producer flush finished")
