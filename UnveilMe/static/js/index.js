$(document).ready(function () {
    const socket = io();

    function setup(rooms) {
        const roomsContainer = $('#rooms');
        roomsContainer.empty();
        rooms.forEach(function (room) {
            const roomElement = $('<div></div>', { id: room });
            roomElement.html(`<h2>${room}</h2>`);
            roomElement.on('click', function () {
                const username = $('#username').val();
                if (username !== '') {
                    window.location.href = `/room/${room}/${username}`;
                }
            });
            roomsContainer.append(roomElement);
        });
    }

    $('#create').click(function () {
        const username = $('#username').val();
        const room = $('#room').val();
        if (username !== '' && room !== '') {
            socket.emit('join', { username: username, room: room });
            window.location.href = `/room/${room}/${username}`;
        } else {
            alert('Please enter both a username and a room name.');
        }
    });

    socket.on('update_rooms', function (rooms) {
        setup(rooms);
    });

    // Fetch existing rooms on page load
    $.getJSON('/rooms', function (rooms) {
        setup(rooms);
    });
});