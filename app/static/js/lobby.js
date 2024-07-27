import * as SocketModule from './socket.js'

document.addEventListener('DOMContentLoaded', () => {

    const leaveButton = document.getElementById('leave');
    const toggleReadyButton = document.getElementById('toggleready');
    const playerContainer = document.getElementById('player-container');

    SocketModule.render_lobby_socket(renderLobbyContainer);

    function renderLobbyContainer(lobby) {
        console.log('diocane');
        const players = lobby.players;
        playerContainer.innerHTML = '';

        for (const [key, value] of Object.entries(players)) {
            const playerElement = document.createElement('div');
            playerElement.id = key;
            playerElement.innerHTML = `<h2>${key}</h2>`;
            playerElement.style.backgroundColor = value.is_ready ? 'green' : 'red';
            playerContainer.appendChild(playerElement);
        }
    }


    leaveButton.addEventListener('click', () => {
        const urlParams = new URLSearchParams(window.location.search);
        const username = urlParams.get('username');
        const lobbyName = urlParams.get('lobbyName');
        SocketModule.leave_lobby(username, lobbyName);
        window.location.href = `/`;
    });

    toggleReadyButton.addEventListener('click', () => {
        const urlParams = new URLSearchParams(window.location.search);
        const username = urlParams.get('username');
        const lobbyName = urlParams.get('lobbyName');
        SocketModule.toggle_ready(username, lobbyName);
    });


});