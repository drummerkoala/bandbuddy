from flask import current_app
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.active = True
        self.is_admin = False

    def get_id(self):
        return self.user_id

    @property
    def is_active(self):
        return self.active


def get_user(user_id):
    db = current_app.config["db"]
    user_id = db.get_user_with_id(user_id)
    if user_id is not None:
        user = User(user_id[0], user_id[1], user_id[2])
    else:
        return None
    if user is not None:
        user.is_admin = user.username in current_app.config["ADMIN_USERS"]
    return user
    