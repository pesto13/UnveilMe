import { io } from 'https://cdn.socket.io/4.7.5/socket.io.esm.min.js';

const socket = io.connect('http://127.0.0.1:5000/');

const setup_socket = ((updateLobbiesContainer) => {
    socket.on('connect', () => {
        console.log('connesso');
    });

    socket.on('disconnect', () => {
        console.log('disconnesso');
    });

    socket.on('message', message => {
        alert(message);
    });
});

const game_socket = ((updateLobbiesContainer) => {
    socket.on('render_lobbies', (data) => {
        console.log(data)
        console.log(data.lobbies)
        updateLobbiesContainer(data.lobbies);
    })
})


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


export { setup_socket, game_socket, create_lobby, join_lobby, leave_lobby, start_game, vote_player, add_point }