import io from 'socket.io-client';

const socket = io();

function subscribeToEvent(cb) {
    socket.on('event', EventData => {
        console.log(EventData);
        cb(null, EventData);
    });
};

export { subscribeToEvent };