from pathlib import Path

from grpc import ServicerContext

from contracts.services.users.rpc_get_user_pb2 import GetUserRequest, GetUserResponse
from contracts.services.users.users_service_pb2_grpc import UsersServiceServicer
from tests.mock.grpc.tools import get_scenario_grpc
from tests.tools.date import MockLoader
from tests.tools.logger import get_test_logger


loader = MockLoader(
    root=Path('./tests/mock/grpc/data/users'),
    logger=get_test_logger("USERS_SERVICE_MOCK_LOADER")
)

class UsersMockService(UsersServiceServicer):
    async def GetUser(self, request: GetUserRequest, context: ServicerContext) -> GetUserResponse:
        scenario = await get_scenario_grpc(context)

        return await loader.load_grpc(
            file=f"GetUser/{scenario}.json",
            model=GetUserResponse
        )