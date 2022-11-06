import random
from dataclasses import dataclass

import faker


GENDERS = ("Male", "Female")


@dataclass(frozen=True)
class TestUser:
    first_name: str
    last_name: str
    email: str
    password: str
    gender: str


Active_User = TestUser(
    first_name="user",
    last_name="testov",
    email="testov_user@mail.ru",
    password="password",
    gender=GENDERS[0]
)

fake = faker.Faker()

FakeUser = TestUser(
    first_name=fake.first_name(),
    last_name=fake.last_name(),
    email=fake.email(),
    password=fake.password(),
    gender=random.choice(GENDERS)
)
