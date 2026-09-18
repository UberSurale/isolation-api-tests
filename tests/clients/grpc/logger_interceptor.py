from logging import Logger

from grpc import UnaryUnaryClientInterceptor


class GRPCLoggerInterceptor(UnaryUnaryClientInterceptor):
    def __init__(self, logger: Logger):
        self.logger = logger

    def intercept_unary_unary(self, continuation, client_call_details, request):
        self.logger.info(f"REQUEST: ${client_call_details.method}")

        response = continuation(client_call_details, request)

        self.logger.info(f"RESPONSE: {client_call_details.method}")

        return response