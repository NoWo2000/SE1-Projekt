import openSocket from 'socket.io-client';

const socket = openSocket('http://localhost:8000');

function subscribeToEvent(cb) {
    socket.on('event', EventData => cb(null, EventData));
};

export { subscribeToEvent };