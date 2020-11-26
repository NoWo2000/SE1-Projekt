import openSocket from 'socket.io-client';

const socket = openSocket('http://localhost:8000');

function subscribeToEvent(cb) {
    socket.on('event', timestamp => cb(null, timestamp));
    socket.emit('subscribeToEvent', 1000);
}

export default { subscribeToEvent };