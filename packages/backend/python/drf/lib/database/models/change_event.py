from faker import Faker
from datetime import datetime
import random
from .base_pay import BasePay


class ChangeEventField:
    TITLE = "title"
    STATUS = "status"


class Change:
    def __init__(self, old_value, new_value):
        self.old_value = old_value
        self.new_value = new_value


class ChangeEvent:
    def __init__(
        self,
        user_id,
        field,
        old_value,
        new_value,
        position_id=None,
    ):
        self.user_id = user_id
        self.field = field
        self.old_value = old_value
        self.new_value = new_value
        self.position_id = position_id
        self.created_at = datetime.now()

    def __repr__(self):
        return f"ChangeEvent(id={self.change_event_id}, user_id={self.user_id}, field={self.field}, old_value={self.old_value}, new_value={self.new_value}, position_id={self.position_id}, created_at={self.created_at})"


def generate_mock_changes(db, users, positions):
    fake = Faker()
    changes = []

    for _ in range(20):
        user = random.choice(users)
        position = random.choice(positions)

        simple_change = ChangeEvent(
            user.user_id,
            ChangeEventField.TITLE,
            fake.job(),
            position.title,
            position.position_id,
        )
        res = db.changeevents.insert_one(simple_change.__dict__)
        print(res)
        changes.append(simple_change)

    return changes
