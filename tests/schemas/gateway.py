from pydantic import BaseModel

from tests.schemas.accounts import AccountTestSchema
from tests.schemas.cards import CardTestSchema
from tests.schemas.users import UserTestSchema


class UserDetailsTestSchema(BaseModel):
    user: UserTestSchema
    accounts: list[AccountTestSchema]


class GetUserDetailsResponseTestSchema(BaseModel):
    details: UserDetailsTestSchema


class AccountDetailsTestSchema(BaseModel):
    cards: list[CardTestSchema]
    account: AccountTestSchema


class GetAccountDetailsResponseTestSchema(BaseModel):
    details: AccountDetailsTestSchema
