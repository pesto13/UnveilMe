from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, join_room, leave_room, emit
from .classes.classes import Room, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

rooms: dict[str, Room] = {}


@app.route('/')
def index():
    return render_template('index.html', rooms=list(rooms.keys()))


@app.route('/room/<room>/<username>')
def room(room, username):
    return render_template('room.html', room=room, username=username)


@app.route('/rooms')
def get_rooms():
    return jsonify(list(rooms.keys()))


@socketio.on('join')
def handle_join(data):
    room_name = data['room']
    username = data['username']
    join_room(room_name)

    if room_name not in rooms:
        rooms[room_name] = Room(room_name)
    room = rooms[room_name]

    user = User(username)
    room.add_user(user)

    emit('update_users', room.get_users(), room=room_name)
    emit('update_rooms', list(rooms.keys()), broadcast=True)


@socketio.on('leave')
def handle_leave(data):
    room_name = data['room']
    username = data['username']
    leave_room(room_name)

    if room_name in rooms:
        room = rooms[room_name]
        room.remove_user(username)
        if room.is_empty():
            del rooms[room_name]

    emit('update_users', room.get_users()
         if room_name in rooms else {}, room=room_name)
    emit('update_rooms', list(rooms.keys()), broadcast=True)


@socketio.on('toggle_status')
def handle_toggle_status(data):
    room_name = data['room']
    username = data['username']

    if room_name in rooms and username in rooms[room_name].users:
        user = rooms[room_name].users[username]
        user.toggle_status()
        emit('update_users', rooms[room_name].get_users(), room=room_name)
