$(document).ready(function () {
    const socket = io();
    const room = "{{ room }}";
    const username = "{{ username }}";

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
            $('#users').append('<p>' + username + ': ' + status + '</p>');
        });
    });

    $(window).on('beforeunload', function () {
        socket.emit('leave', { username: username, room: room });
    });
});