from faker import Faker
import random
from .base_pay import BasePay


class PositionStatus:
    ACTIVE = "active"
    INACTIVE = "inactive"


class Position:
    def __init__(
        self, title, status, base_pay_currency, base_pay_amount, position_id=None
    ):
        self.position_id = position_id
        self.title = title
        self.status = status
        self.base_pay_currency = base_pay_currency
        self.base_pay_amount = base_pay_amount

    def __repr__(self):
        return f"Position(id={self.position_id}, title={self.title}, status={self.status}, base_pay_currency={self.base_pay_currency}, base_pay_amount={self.base_pay_amount})"


def generate_mock_positions(db, count=10):  # Replace with your own password
    fake = Faker()
    positions = []

    for _ in range(count):
        position = Position(
            fake.job(),
            PositionStatus.ACTIVE,
            fake.currency(),
            random.randint(1000, 10000),
            "P-000{}".format(random.randint(1, 9999)),
        )
        position_id = db.positions.insert_one(position.__dict__).inserted_id
        position.position_id = position_id
        positions.append(position)
    return positions
