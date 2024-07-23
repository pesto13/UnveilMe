
class Player:
    def __init__(self, username, points, is_ready):
        self.username = username
        self.points = points
        self.is_ready = is_ready


class Lobby:

    def __init__(self, turns: int = 10) -> None:
        self.turns = turns
        self.players = {}
