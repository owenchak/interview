from faker import Faker

class User:
    def __init__(self, name: str, user_id=None):
        self.user_id = user_id  # Store the MongoDB ObjectId
        self.name = name

    def __repr__(self):
        return f"User(id={self.user_id}, name={self.name}, email={self.email}, created_at={self.created_at})"


def generate_mock_users(db, count=10):
    fake = Faker()
    users = []

    for _ in range(count):
        # Generate a fake name
        name = fake.name()
        
        # Create a User instance
        user = User(name=name)
        
        # Insert into MongoDB and get the inserted _id
        user_id = db.users.insert_one({"name": user.name}).inserted_id
        user.user_id = user_id  # Assign MongoDB ObjectId to the User instance
        users.append(user)

    return users
