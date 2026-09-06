from pathlib import Path
import uuid

from fastapi import APIRouter
from fastapi.params import Depends

from tests.context.scenario import Scenario
from tests.mock.http.tools import get_scenario_http
from tests.schemas.users import GetUserResponseTestSchema
from tests.tools.logger import get_test_logger
from tests.tools.mock import MockLoader
from tests.tools.routes import APITestRoutes


loader = MockLoader(
    root = Path("./tests/mock/http/data/users"),
    logger=get_test_logger("USERS_SERVICE_MOCK_LOADER")
)

users_mock_router = APIRouter(
    prefix=APITestRoutes.USERS,
    tags=[APITestRoutes.USERS]
)

@users_mock_router.get("/{user_id}", response_model=GetUserResponseTestSchema)
async def get_user_view(
    user_id: uuid.UUID,
    scenario: Scenario = Depends(get_scenario_http),
):
    return await loader.load_http(
        file=f"get_user/{scenario}.json",
        model=GetUserResponseTestSchema
    )