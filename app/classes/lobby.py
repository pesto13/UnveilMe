
class Player:
    def __init__(self, username, points, is_ready):
        self.username = username
        self.points = points
        self.is_ready = is_ready

    def to_dict(self):
        return {
            'username': self.username,
            'points': self.points,
            'is_ready': self.is_ready
        }


class Lobby:

    def __init__(self, turns: int = 10) -> None:
        self.turns = turns
        self.players = {}

    def to_dict(self):
        return {
            'turns': self.turns,
            'players': {
                username: player.to_dict() for username, player
                in self.players.items()
            }
        }
