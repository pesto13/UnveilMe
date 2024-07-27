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
    def create_lobby(data):
        # username = data['username']
        lobby_name = data['lobby_name']

        if lobby_name in lobbies:
            send('Lobby already exists')
            return

        lobbies[lobby_name] = Lobby()
        emit('render_lobbies', {'lobbies': get_lobbies_data()}, broadcast=True)

    @socketio.event
    def join_lobby(data):
        username = data['username']
        lobby_name = data['lobby_name']
        if username in lobbies[lobby_name].players:
            return

        lobbies[lobby_name].players[username] = Player(username, 0, False)
        join_room(lobby_name)

        emit('render_lobby', {
            'lobby': lobbies[lobby_name].to_dict()
        }, to=lobby_name)

    @socketio.event
    def leave_lobby(data):
        username = data['username']
        lobby_name = data['lobby_name']
        if username not in lobbies[lobby_name].players:
            return

        del lobbies[lobby_name].players[username]
        leave_room(lobby_name)

        emit('render_lobby', {
            'lobby': lobbies[lobby_name].to_dict()
        }, to=lobby_name)

    @socketio.event
    def toggle_ready(data):
        username = data['username']
        lobby_name = data['lobby_name']
        if username not in lobbies[lobby_name].players:
            return

        p = lobbies[lobby_name].players[username]
        p.is_ready = not p.is_ready

    @socketio.event
    def start_game(data):
        pass

    ##############


def start_game(data):
    lobby_name = data['lobby_name']
    # Logica per iniziare la partita
    emit('start_game', 'The game has started!', to=lobby_name)
