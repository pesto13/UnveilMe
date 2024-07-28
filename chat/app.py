from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

users = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/room/<room>/<username>')
def room(room, username):
    return render_template('room.html', room=room, username=username)


@socketio.on('join')
def handle_join(data):
    room = data['room']
    username = data['username']
    join_room(room)
    if room not in users:
        users[room] = {}
    users[room][username] = 'inactive'
    emit('update_users', users[room], room=room)


@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    username = data['username']
    leave_room(room)
    if room in users and username in users[room]:
        del users[room][username]
        emit('update_users', users[room], room=room)


@socketio.on('toggle_status')
def handle_toggle_status(data):
    room = data['room']
    username = data['username']
    if room in users and username in users[room]:
        users[room][username] = 'active' if users[room][username] == 'inactive' else 'inactive'
        emit('update_users', users[room], room=room)


if __name__ == '__main__':
    socketio.run(app, debug=True)
