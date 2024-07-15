document.addEventListener('DOMContentLoaded', () => {
    const socket = io.connect('http://' + document.domain + ':' + location.port);

    // Elementi DOM
    const usernameInput = document.getElementById('username');
    const lobbyIdInput = document.getElementById('lobby_id');
    const joinButton = document.getElementById('join');
    const leaveButton = document.getElementById('leave');
    const readyButton = document.getElementById('ready');
    const updatePointsButton = document.getElementById('update_points');
    const messagesDiv = document.getElementById('messages');
    const statusDiv = document.getElementById('status');

    // Aggiungi messaggi al div dei messaggi
    function addMessage(message) {
        const p = document.createElement('p');
        p.textContent = message;
        messagesDiv.appendChild(p);
    }

    // Eventi WebSocket
    socket.on('message', function (message) {
        addMessage(message);
    });

    // Eventi di connessione
    socket.on('connect', function () {
        statusDiv.textContent = 'Connected to the server.';
    });

    socket.on('disconnect', function () {
        statusDiv.textContent = 'Disconnected from the server.';
    });

    socket.on('start_game', function (message) {
        addMessage(message);
    });

    // Eventi dei pulsanti
    joinButton.addEventListener('click', () => {
        socket.emit('join', {
            username: usernameInput.value,
            lobby_id: lobbyIdInput.value
        });
    });

    leaveButton.addEventListener('click', () => {
        socket.emit('leave', {
            username: usernameInput.value,
            lobby_id: lobbyIdInput.value
        });
    });

    readyButton.addEventListener('click', () => {
        socket.emit('change_is_ready', {
            username: usernameInput.value,
            lobby_id: lobbyIdInput.value
        });
    });

    updatePointsButton.addEventListener('click', () => {
        socket.emit('update_points', {
            username: usernameInput.value,
            lobby_id: lobbyIdInput.value
        });
    });
});
