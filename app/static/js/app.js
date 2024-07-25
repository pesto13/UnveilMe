import * as SocketModule from './socket.js'

document.addEventListener('DOMContentLoaded', () => {

    SocketModule.setup_socket();

    const usernameInput = document.getElementById('username');
    const lobbyNameInput = document.getElementById('lobby_name');
    const createButton = document.getElementById('create');
    const leaveButton = document.getElementById('leave');
    const readyButton = document.getElementById('ready');

    const lobbiesContainer = document.getElementById('Lobbies-container');

    createButton.addEventListener('click', () => {
        const username = usernameInput.value;
        const lobbyName = lobbyNameInput.value;

        if (username && lobbyName) {
            SocketModule.create_lobby(username, lobbyName)
            console.log('creata')
        } else {
            console.log('inserisci valori')
        }
    });



});
