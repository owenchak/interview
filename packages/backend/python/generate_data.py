from drf.lib.database.models.user import generate_mock_users
from drf.lib.database.client import get_db
from drf.lib.database.models.position import generate_mock_positions
from drf.lib.database.models.change_event import generate_mock_changes


def delete_all_data(db):
    db.positions.delete_many({})
    db.users.delete_many({})
    db.changeevents.delete_many({})


db = get_db()

delete_all_data(db)
users = generate_mock_users(db, 10)
positions = generate_mock_positions(db, 10)
changes = generate_mock_changes(db, users, positions)

