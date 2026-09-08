import asyncio
from concurrent import futures
from contracts.services.accounts import accounts_service_pb2, accounts_service_pb2_grpc
from contracts.services.cards import cards_service_pb2, cards_service_pb2_grpc
from contracts.services.users import users_service_pb2, users_service_pb2_grpc
from tests.config import test_settings

import grpc

from tests.mock.grpc.api.accounts import AccountsMockService
from tests.mock.grpc.api.cards import CardsMockService
from tests.mock.grpc.api.users import UsersMockService

from grpc_reflection.v1alpha import reflection


async def serve():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))

    server.add_insecure_port(test_settings.mock_grpc_server.url)

    users_service_pb2_grpc.add_UsersServiceServicer_to_server(UsersMockService(), server)
    cards_service_pb2_grpc.add_CardsServiceServicer_to_server(CardsMockService(), server)
    accounts_service_pb2_grpc.add_AccountsServiceServicer_to_server(AccountsMockService(), server)

    reflection.enable_server_reflection(
        (
            reflection.SERVICE_NAME,
            users_service_pb2.DESCRIPTOR.services_by_name['UsersService'].full_name,
            cards_service_pb2.DESCRIPTOR.services_by_name['CardsService'].full_name,
            accounts_service_pb2.DESCRIPTOR.services_by_name['AccountsService'].full_name
        ),
        server
    )

    await server.start()
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())