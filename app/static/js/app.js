import * as SocketModule from './socket.js'

document.addEventListener('DOMContentLoaded', () => {

    SocketModule.setup_socket();
    SocketModule.game_socket(updateLobbiesContainer);

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

    // funzioni

    function updateLobbiesContainer(lobbies) {
        lobbiesContainer.innerHTML = '';
        for (const [lobbyName, lobby] of Object.entries(lobbies)) {
            const lobbyElement = document.createElement('div');
            lobbyElement.classList.add('lobby');
            lobbyElement.innerHTML = `
                <h2>${lobbyName}</h2>
                <p>Players: ${Object.keys(lobby.players).length}</p>
                <button onclick="joinLobby('${lobbyName}')">Join Lobby</button>
            `;
            lobbiesContainer.appendChild(lobbyElement);
        }
    }



});
