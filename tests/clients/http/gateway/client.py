import uuid

from httpx import Response

from tests.clients.http.client import HTTPTestClient, build_http_test_client
from tests.context.base import RequestContext
from tests.schemas.gateway import GetAccountDetailsResponseTestSchema, GetUserDetailsResponseTestSchema
from tests.tools import allure
from tests.tools.logger import get_test_logger
from tests.tools.routes import APITestRoutes
from tests.tools.fakers import fake
from tests.config import test_settings


class GatewayHTTPTestClient(HTTPTestClient):

    @allure.step("Get user details")
    def get_user_details_api(
        self,
        user_id: uuid.UUID,
        context: RequestContext,
    ) -> Response:
        return self.get(
            f"{APITestRoutes.GATEWAY}/user-details/{user_id}",
            context=context,
        )


    @allure.step("Get account details")
    def get_account_details_api(
        self,
        account_id: uuid.UUID,
        context: RequestContext,
    ) -> Response:
        return self.get(
            f"{APITestRoutes.GATEWAY}/account-details/${account_id}",
            context=context
        )


    def get_user_details(self, context: RequestContext) -> GetUserDetailsResponseTestSchema:
        response = self.get_user_details_api(fake.uuid(), context)
        response.raise_for_status()
        return GetUserDetailsResponseTestSchema.model_validate_json(response.text)


    def get_account_details(self, context: RequestContext) -> GetAccountDetailsResponseTestSchema:
        response = self.get_account_details_api(fake.uuid(), context)
        response.raise_for_status()
        return GetAccountDetailsResponseTestSchema.model_validate_json(response.text)


def build_gateway_http_test_client() -> GatewayHTTPTestClient:
    client = build_http_test_client(
        logger=get_test_logger("GATEWAY_HTTP_TEST_CLIENT"),
        config=test_settings.gateway_http_client,
    )
    return GatewayHTTPTestClient(client=client)

