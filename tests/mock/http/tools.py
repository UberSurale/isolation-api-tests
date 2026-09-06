from typing import Annotated

from fastapi import HTTPException, Header, status

from tests.context.scenario import Scenario


def get_scenario_http(
        scenario: Annotated[Scenario | None, Header(alias="X-Test-Scenario")] = None
) -> Scenario:
    if not scenario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing X-Test-Scenario header",
        )
    return scenario