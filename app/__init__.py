from flask import Flask


def create_app():
    app = Flask(__name__)
    # app.config.from_object('config.Config')

    with app.app_context():
        # Importa le route
        # from . import routes

        # Inizializza le estensioni
        # db.init_app(app)
        # migrate.init_app(app, db)

        return app
