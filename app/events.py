from flask_socketio import send, emit, join_room, leave_room
from .classes.lobby import Lobby, Player

from collections import defaultdict

lobbies = defaultdict(lambda: Lobby(id=""))


def register_events(socketio):

    @socketio.on('message')
    def handle_message(message):
        send(f"Echo: {message}", broadcast=True)

    @socketio.on('connect')
    def handle_connect():
        emit('message', 'Welcome to the WebSocket server!')

    @socketio.on('disconnect')
    def handle_disconnect():
        pass

    #############

    @socketio.on('join')
    def on_join(data):
        username = data.get('username')
        lobby_id = data.get('lobby_id')
        player = Player(username=username, points=0, is_ready=False)
        this_lobby = lobbies.setdefault(lobby_id, Lobby(lobby_id))
        if username in this_lobby.players:
            send('You cant rejoin the room')
            return

        this_lobby.players[username] = player
        join_room(lobby_id)
        send(
            f'{username} has joined the lobby {lobby_id}',
            room=lobby_id
        )

    @socketio.on('leave')
    def on_leave(data):
        username = data.get('username')
        lobby_id = data.get('lobby_id')

        leave_room(lobby_id)

        del lobbies[lobby_id].players[username]
        send(
            f'{username} has left the lobby {lobby_id}',
            room=lobby_id
        )

        # if no more players delete the entire lobby
        if len(lobbies[lobby_id].players) == 0:
            del lobbies[lobby_id]

    @socketio.on('toogle_is_ready')
    def on_toggle_ready(data):
        username = data.get('username')
        lobby_id = data.get('lobby_id')

        this_lobby = lobbies.get(lobby_id, None)

        if this_lobby is None:
            raise Exception('Lobby does not exist')

        this_lobby.players[username].is_ready = not (
            this_lobby.players[username].is_ready
        )

        send(
            f'{username} is {
                "ready" if this_lobby.players[username].is_ready
                else "preparing"}',
            room=lobby_id
        )

        if all(p.is_ready for p in this_lobby.players.values()):
            send(
                'All players are ready. The game will start now!',
                room=lobby_id
            )
            start_game(lobby_id)

    ##############

    @socketio.on('update_points')
    def on_update_points(data):
        username = data.get('username')
        lobby_id = data.get('lobby_id')

        this_lobby = lobbies[lobby_id]
        this_lobby.players[username].points += 1
        send(
            f'{username} now has {
                this_lobby.players[username].points} points',
            room=lobby_id
        )


def start_game(lobby_id):
    # Logica per iniziare la partita
    emit('start_game', 'The game has started!', room=lobby_id)
