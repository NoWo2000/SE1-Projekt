const io = require('socket.io')();

io.on('connection', (client) => {
    // here you can start emitting events to the client 
    client.on('subscribeToEvent', (interval) => {
        console.log('client is subscribing to event with interval ', interval);
        setInterval(() => {
            client.emit('event', new Date());
        }, interval);
    });
});

const port = 8000;
io.listen(port);
console.log('listening on port ', port);