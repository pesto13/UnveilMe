$(document).ready(() => {
    const socket = io();

    console.log('sono in game');
    // $.each(users, (key, value) => {

    //     // console.log(status)
    //     const $pdiv = $('<div></div>');
    //     $pdiv.text(value)
    //     $pdiv.attr('id', value)
    //     $('#users-container').append($pdiv);
    // });

    socket.on('fetch_question', function (qst) {
        console.log('lol')
        $('#question').text(qst);
    });

    socket.emit('ask_question', { room: room })

});

