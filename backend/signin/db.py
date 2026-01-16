from global_service.db import get_database


db = get_database()
user = db.get_collection("User")


def addUser(new_user):
    data = user.insert_one(new_user)
    print(data)