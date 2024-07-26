from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/lobby.html')
def lobby():
    lobby_name = request.args.get('lobbyName')
    username = request.args.get('username')
    return render_template(
        'lobby.html', lobby_name=lobby_name, username=username)
