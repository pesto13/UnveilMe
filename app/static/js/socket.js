import { io } from 'https://cdn.socket.io/4.7.5/socket.io.esm.min.js';

const socket = io.connect('http://127.0.0.1:5000/');

const setup_socket = (() => {
    socket.on('connect', () => {
        console.log('connesso con: ', socket.id);
    });

    socket.on('disconnect', () => {
        console.log('disconnesso con: ', socket.id);
    });

    socket.on('message', message => {
        alert(message);
    });
});

// middleware
const render_lobbies_socket = ((updateLobbiesContainer) => {
    console.log('eccoci1')
    socket.on('render_lobbies', (data) => {
        updateLobbiesContainer(data.lobbies);
    });
});

const render_lobby_socket = ((renderLobbyContainer) => {
    console.log('eccoci2')
    socket.on('render_lobby', function (data) {
        console.log('ma perche');
        renderLobbyContainer(data.lobby);
    });
});

//Creazione Lobby

const create_lobby = ((username, lobbyName) => {
    socket.emit('create_lobby', username, lobbyName)
});

const join_lobby = ((username, lobbyName) => {
    socket.emit('join_lobby', username, lobbyName)
});

const leave_lobby = ((username, lobbyName) => {
    socket.emit('leave_lobby', username, lobbyName)
});

const toggle_ready = ((username, lobbyName) => {
    socket.emit('toggle_ready', username, lobbyName)
});

// game - fase di gioco

const start_game = ((lobbyName) => {
    socket.emit('start_game', lobbyName)
});

const vote_player = ((username, voted_player, lobbyName) => {
    socket.emit('vote_player', username, voted_player, lobbyName)
});

const add_point = ((voted_player, lobbyName) => {
    socket.emit('vote_player', voted_player, lobbyName)
});


export {
    setup_socket, render_lobbies_socket, render_lobby_socket,
    create_lobby, join_lobby, leave_lobby, toggle_ready,
    start_game, vote_player, add_point
}