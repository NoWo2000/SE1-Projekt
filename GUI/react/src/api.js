import openSocket from 'socket.io-client';

const socket = openSocket('http://localhost:5000/socket.io');

function subscribeToEvent(cb) {
    socket.on('event', EventData => cb(null, EventData));
};

export { subscribeToEvent };