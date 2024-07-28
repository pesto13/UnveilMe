$(document).ready(function () {
    const socket = io();

    socket.emit('join', { username: username, room: room });

    $('#leave').click(function () {
        socket.emit('leave', { username: username, room: room });
        window.location.href = '/';
    });

    $('#toggle').click(function () {
        socket.emit('toggle_status', { username: username, room: room });
    });

    socket.on('update_users', function (users) {
        $('#users').empty();
        $.each(users, function (username, status) {
            // console.log(status)
            const $pdiv = $('<div></div>');
            $pdiv.text(username + ': ' + status)
            $pdiv.attr('id', username)
            $pdiv.css('background', status === true ? 'lightgreen' : 'lightcoral');
            $('#users').append($pdiv);
        });
    });

    socket.on('start_game', () => {
        window.location.href = `/game/${room}/${username}`
    });

    // $(window).on('beforeunload', function () {
    //     socket.emit('leave', { username: username, room: room });
    // });
});