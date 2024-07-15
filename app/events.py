from flask_socketio import send, emit


def register_events(socketio):
    @socketio.on('message')
    def handle_message(message):
        print(f"Received message: {message}")
        # Broadcast il messaggio a tutti i client connessi
        send(f"Echo: {message}", broadcast=True)

    @socketio.on('connect')
    def handle_connect():
        print('Client connected')
        emit('message', 'Welcome to the WebSocket server!')

    @socketio.on('disconnect')
    def handle_disconnect():
        print('Client disconnected')
