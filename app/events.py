from flask_socketio import send, emit, join_room, leave_room
from .classes.lobby import Lobby, Player

lobbies: dict[Lobby] = dict()


def register_events(socketio):

    @socketio.event
    def connect():
        send('Welcome to the UnveilMe server!')

    @socketio.event
    def disconnect():
        pass

    #############

    @socketio.event
    def create_lobby(username, lobby_name):
        print(lobby_name)
        # Ensure that the lobby doesn't already exist
        if lobby_name in lobbies:
            emit('lobby_error', {'message': 'Lobby already exists'})
            return

        lobbies[lobby_name] = Lobby()
        print('Current lobbies:', list(lobbies.keys()))
        emit('lobby_created', {'lobby_name': lobby_name})

    @socketio.event
    def join_lobby(data):
        pass

    @socketio.event
    def leave_lobby(data):
        pass

    @socketio.event
    def start_game(data):
        pass

    ##############


def start_game(lobby_name):
    # Logica per iniziare la partita
    emit('start_game', 'The game has started!', room=lobby_name)
