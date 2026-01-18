# Roadmap.sh Broadcast Server

### What I am Gonna Learn

* Websockets
* Real Time Communication

### Requirements

* [ ] Implement 'broadcast-server start' for starting the server
* [ ] Implement 'broadcast-server connect' for connecting the client to server
* [ ] Listen at spesified port(either configure using command or hardcoded)
* [ ] Handling multiple client
* [ ] Proper disconnect

### Implementation

* [ ] Create a server that listens for incoming connections.
* [ ] When a client connects, store the connection in a list of connected clients.
* [ ] When a client sends a message, broadcast this message to all connected clients.
* [ ] Handle client disconnections and remove the client from the list of connected clients.
* [ ] Implement a client that can connect to the server and send messages.
* [ ] Test the server by connecting multiple clients and sending messages.
* [ ] Implement error handling and graceful shutdown of the server.
