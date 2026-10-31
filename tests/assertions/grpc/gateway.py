from datetime import date

import allure

from contracts.services.accounts.account_pb2 import (
    ACCOUNT_STATUS_ACTIVE,
    ACCOUNT_TYPE_CREDIT_CARD,
    ACCOUNT_TYPE_DEBIT_CARD,
    Account,
)
from contracts.services.cards.card_pb2 import (
    CARD_PAYMENT_SYSTEM_MASTERCARD,
    CARD_PAYMENT_SYSTEM_VISA,
    CARD_STATUS_ACTIVE,
    CARD_STATUS_BLOCKED,
    CARD_TYPE_PHYSICAL,
    CARD_TYPE_VIRTUAL,
    Card,
)
from contracts.services.gateway.account_details_pb2 import AccountDetails
from contracts.services.gateway.rpc_get_account_details_pb2 import GetAccountDetailsResponse
from contracts.services.gateway.rpc_get_user_details_pb2 import GetUserDetailsResponse
from contracts.services.gateway.user_details_pb2 import UserDetails
from contracts.services.users.user_pb2 import User
from tests.assertions.base import assert_equal
from tests.assertions.http.accounts import assert_account
from tests.assertions.http.cards import assert_card
from tests.assertions.http.users import assert_user
from tests.schemas.accounts import AccountTestSchema
from tests.schemas.cards import CardTestSchema
from tests.schemas.gateway import AccountDetailsTestSchema, GetAccountDetailsResponseTestSchema, GetUserDetailsResponseTestSchema, UserDetailsTestSchema
from tests.schemas.users import UserTestSchema
from tests.tools.date import to_proto_test_date
from tests.tools.logger import get_test_logger

logger = get_test_logger("GATEWAY_ASSERTIONS")


@allure.step("Check user details")
def assert_user_details(actual: UserDetails, expected: UserDetails) -> None:
    logger.info("Check user details")

    assert_user(actual.user, expected.user)

    assert_equal(len(actual.accounts), len(expected.accounts), "accounts count")

    for index, account in enumerate(expected.accounts):
        assert_account(actual.accounts[index], account)


@allure.step("Check account details")
def assert_account_details(actual: AccountDetails, expected: AccountDetails) -> None:
    logger.info("Check account details")

    assert_account(actual.account, expected.account)

    assert_equal(len(actual.cards), len(expected.cards), "cards count")

    for index, card in enumerate(expected.cards):
        assert_card(actual.cards[index], card)


@allure.step("Check get user details response")
def assert_get_user_details_response(
    actual: GetUserDetailsResponse,
    expected: GetUserDetailsResponse
) -> None:
    logger.info("Check get user details response")
    assert_user_details(actual.details, expected.details)


@allure.step("Check get account details response")
def assert_get_account_details_response(
    actual: GetAccountDetailsResponse,
    expected: GetAccountDetailsResponse
) -> None:
    logger.info("Check get account details response")

    assert_account_details(actual.details, expected.details)


@allure.step("Check get user details response. User with active credit card account")
def assert_get_user_details_response_user_with_active_credit_card_account(
        actual: GetUserDetailsResponse,
) -> None:
    logger.info("Check get user details response. User with active credit card account")

    expected = GetUserDetailsResponse(
        details=UserDetails(
            user=User(
                id="8b0e7c2a-1b6a-4e5d-9f1a-1b3f2a7c9e21",
                email="anna.ivanova@example.com",
                last_name="Иванова",
                first_name="Анна",
                middle_name="Алексеевна",
                phone_number="+79005554433",
            ),
            accounts=[
                Account(
                    id="99999999-aaaa-4bbb-8ccc-000000000001",
                    type=ACCOUNT_TYPE_CREDIT_CARD,
                    status=ACCOUNT_STATUS_ACTIVE,
                    user_id="3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    balance=-15230.75,
                )
            ],
        )
    )
    assert_get_user_details_response(actual, expected)


@allure.step("Check get account details response. User with active debit card account")
def assert_get_account_details_response_user_with_active_debit_card_account(
        actual: GetAccountDetailsResponse,
) -> None:
    logger.info("Check get account details response. User with active debit card account")

    expected = GetAccountDetailsResponse(
        details=AccountDetails(
            account=Account(
                id="6e4b92a1-73dc-4f08-b561-29c7a845e013",
                type=ACCOUNT_TYPE_DEBIT_CARD,
                status=ACCOUNT_STATUS_ACTIVE,
                user_id="a72f35c8-614e-4b09-9d63-5802fa71bc46",
                balance=-8745.20,
            ),
            cards=[
                Card(
                    id="7f3a91c2-5d84-4e17-9b63-1a8c52d740ef",
                    pin="4821",
                    cvv="315",
                    type=CARD_TYPE_VIRTUAL,
                    status=CARD_STATUS_ACTIVE,
                    account_id="c4e82a17-9f35-4b61-a728-53d91e6f8042",
                    card_number="4000000000000001",
                    card_holder="ALEXEY SMIRNOV",
                    expiry_date=to_proto_test_date(date(2029, 3, 31)),
                    payment_system=CARD_PAYMENT_SYSTEM_VISA,
                ),
                Card(
                    id="b62e40d9-1837-4ac5-8f21-76d3c950a4be",
                    pin="7364",
                    cvv="821",
                    type=CARD_TYPE_PHYSICAL,
                    status=CARD_STATUS_ACTIVE,
                    account_id="c4e82a17-9f35-4b61-a728-53d91e6f8042",
                    card_number="5555555555554444",
                    card_holder="ALEXEY SMIRNOV",
                    expiry_date=to_proto_test_date(date(2030, 8, 31)),
                    payment_system=CARD_PAYMENT_SYSTEM_MASTERCARD,
                ),
                Card(
                    id="e91c73a5-2b46-4d80-a1f9-6385be0274cd",
                    pin="1593",
                    cvv="604",
                    type=CARD_TYPE_VIRTUAL,
                    status=CARD_STATUS_BLOCKED,
                    account_id="8a17d3c9-42e6-4f50-b981-27ac6d5e1038",
                    card_number="4000000000000027",
                    card_holder="MARIA IVANOVA",
                    expiry_date=to_proto_test_date(date(2028, 11, 30)),
                    payment_system=CARD_PAYMENT_SYSTEM_VISA,
                ),
                Card(
                    id="4c8b15e7-9032-46ad-b7f1-2d694a83c5e0",
                    pin="9057",
                    cvv="472",
                    type=CARD_TYPE_PHYSICAL,
                    status=CARD_STATUS_ACTIVE,
                    account_id="8a17d3c9-42e6-4f50-b981-27ac6d5e1038",
                    card_number="5555555555555557",
                    card_holder="MARIA IVANOVA",
                    expiry_date=to_proto_test_date(date(2029, 5, 31)),
                    payment_system=CARD_PAYMENT_SYSTEM_MASTERCARD,
                ),
            ],
        )
    )
    assert_get_account_details_response(actual, expected)