from flask import Flask
from flask_socketio import SocketIO

# Crea l'istanza dell'app Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# Configura SocketIO
socketio = SocketIO(app, cors_allowed_origins='*',
                    logger=True, engineio_logger=True)


def create_app():
    # Crea una nuova istanza dell'app
    app = Flask(__name__)
    # app.config.from_object('config.Config')

    # Inizializza le estensioni
    socketio.init_app(app)

    # Registra le blueprints
    from .routes import main
    app.register_blueprint(main)

    from .events import register_events
    register_events(socketio)

    return app
