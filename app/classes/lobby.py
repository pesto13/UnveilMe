
class Player:
    def __init__(self, username, points, is_ready):
        self.username = username
        self.points = points
        self.is_ready = is_ready


class Lobby:

    def __init__(self, id: int, turns: int = 10) -> None:
        self.id = id
        self.turns = turns
        self.players = {}
