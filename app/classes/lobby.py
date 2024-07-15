import collections

Player = collections.namedtuple('Player', 'Username Points'.split())


class Lobby:

    def __init__(self, id: int, turns: int, players: list) -> None:
        self.id = id
        self.turns = turns
        self.players = players
