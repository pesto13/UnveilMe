from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

users = {}
rooms = set()


@app.route('/')
def index():
    return render_template('index.html', rooms=list(rooms))


@app.route('/room/<room>/<username>')
def room(room, username):
    return render_template('room.html', room=room, username=username)


@app.route('/rooms')
def get_rooms():
    return jsonify(list(rooms))


@socketio.on('join')
def handle_join(data):
    room = data['room']
    username = data['username']
    join_room(room)
    rooms.add(room)
    if room not in users:
        users[room] = {}
    users[room][username] = 'inactive'
    emit('update_users', users[room], room=room)
    emit('update_rooms', list(rooms), broadcast=True)


@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    username = data['username']
    leave_room(room)
    if room in users and username in users[room]:
        del users[room][username]
        if not users[room]:  # If the room is empty, remove it
            del users[room]
            rooms.remove(room)
        emit('update_users', users[room], room=room)
        emit('update_rooms', list(rooms), broadcast=True)


@socketio.on('toggle_status')
def handle_toggle_status(data):
    room = data['room']
    username = data['username']
    if room in users and username in users[room]:
        users[room][username] = 'active' if users[room][username] == 'inactive' else 'inactive'
        emit('update_users', users[room], room=room)
