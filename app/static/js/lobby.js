import * as SocketModule from './socket.js'

document.addEventListener('DOMContentLoaded', () => {

    const leaveButton = document.getElementById('leave');
    const toggleReadyButton = document.getElementById('toggleready');
    const playerContainer = document.getElementById('player-container');

    SocketModule.render_lobby_socket(renderLobbyContainer);

    function renderLobbyContainer(lobby) {
        console.log('diocane')
        players = lobby.players;
        playerContainer.innerHTML = '';
        const playerElement = document.createElement('div');
        for (const [key, value] of Object.entries(players)) {
            playerElement.id = key;
            playerElement.innerHTML = `<h2>${key}</h2 >`;
            playerElement.style.backgroundcolor = value.is_ready ? 'green' : 'red'
        }
        playerContainer.appendChild(playerElement);
    }

    leaveButton.addEventListener('click', () => {
        SocketModule.leave_lobby('franco', 'xxx');
        window.location.href = `/`;
    });

    toggleReadyButton.addEventListener('click', () => {
        SocketModule.toggle_ready('franco', 'xxx');
    });


});