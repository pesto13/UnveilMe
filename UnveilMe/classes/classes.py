class User:
    def __init__(self, username):
        self.username = username
        self.is_ready = False

    def toggle_status(self):
        self.is_ready = not self.status


class Room:
    def __init__(self, name):
        self.name = name
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]

    def is_empty(self):
        return not bool(self.users)

    def get_users(self):
        return {
            username: user.is_ready for username, user in self.users.items()
        }
