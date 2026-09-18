from logging import Logger

from httpx import Client, Headers, QueryParams, Response

from tests.clients.http.logger_event_hook import HTTPLoggerEventHook
from tests.context.base import RequestContext, build_http_test_headers
from tests.tools import allure
from tests.tools.config.http import HTTPClientTestConfig


class HTTPTestClient:

    def __init__(self, client: Client) -> None:
        self.client = client


    @allure.step("Make GET request to {url}")
    def get(
        self,
        url: str,
        params: QueryParams | None = None,
        context: RequestContext | None = None,
    ) -> Response:
        headers = Headers()

        if context:
            headers = Headers(build_http_test_headers(context))

        return self.client.get(
            url=url,
            params=params,
            headers=headers
        )


    def build_http_test_clint(
        logger: Logger,
        config: HTTPClientTestConfig
    ):
        logger_event_hook = HTTPLoggerEventHook(logger=logger)

        return Client(
            timeout=config.timeout,
            base_url=str(config.url),
            event_hooks={
                "request": [logger_event_hook.request],
                "response": [logger_event_hook.response],
            }
        )