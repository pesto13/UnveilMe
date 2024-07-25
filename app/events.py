from flask_socketio import send, emit, join_room, leave_room
from .classes.lobby import Lobby, Player

lobbies: dict[str, Lobby] = dict()


def get_lobbies_data():
    return {
        lobby_name: lobby.to_dict() for lobby_name, lobby in lobbies.items()
    }


def register_events(socketio):

    @socketio.event
    def connect():
        if lobbies is not None:
            emit('render_lobbies', {'lobbies': get_lobbies_data()})

    @socketio.event
    def disconnect():
        pass

    #############

    @socketio.event
    def create_lobby(username, lobby_name):
        print(lobby_name)
        # Ensure that the lobby doesn't already exist
        if lobby_name in lobbies:
            send('Lobby already exists')
            return

        lobbies[lobby_name] = Lobby()
        emit('lobby_created', {'lobby_name': lobby_name})
        emit('render_lobbies', {'lobbies': get_lobbies_data()})
        lobbies[lobby_name].players[username] = Player(username, 0, False)

    @socketio.event
    def join_lobby(username, lobby_name):
        if username in lobbies[lobby_name].lobbies:
            print('gia presente')

        lobbies[lobby_name].players[username] = Player(username, 0, False)

    @socketio.event
    def leave_lobby(username, lobby_name):
        if username not in lobbies[lobby_name].players:
            print('non presente')

        del lobbies[lobby_name].players[username]

    @socketio.event
    def toggle_ready(username, lobby_name):
        if username not in lobbies[lobby_name].players:
            print('non presente')

        is_ready = lobbies[lobby_name].players[username].is_ready
        lobbies[lobby_name].players[username].is_ready != is_ready

    @socketio.event
    def start_game(data):
        pass

    ##############


def start_game(lobby_name):
    # Logica per iniziare la partita
    emit('start_game', 'The game has started!', room=lobby_name)
