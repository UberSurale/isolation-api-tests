from logging import Logger

import grpc

from tests.clients.grpc.logger_interceptor import GRPCLoggerInterceptor
from tests.tools.config.grpc import GRPCClientTestConfig


class GRPCTestClient:
    def __init__(self, channel: grpc.Channel):
        self.channel = channel

    def build_grpc_test_channel(logger: Logger, config: GRPCClientTestConfig) -> grpc.Channel:
        channel = grpc.insecure_channel(config.url)

        return grpc.intercept_channel(channel, GRPCLoggerInterceptor(logger=logger))