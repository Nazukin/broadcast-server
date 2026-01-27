# Roadmap.sh Broadcast Server

### What I am Gonna Learn

* Websockets
* Real Time Communication

### Requirements

* [ ] Implement 'broadcast-server start' for starting the server
* [ ] Implement 'broadcast-server connect' for connecting the client to server
* [X] Listen at spesified port(either configure using command or hardcoded)
* [X] Handling multiple client
* [ ] Proper disconnect

### Implementation

* [X] Create a server that listens for incoming connections.
* [X] When a client connects, store the connection in a list of connected clients.
* [X] When a client sends a message, broadcast this message to all connected clients.
* [ ] Handle client disconnections and remove the client from the list of connected clients.
* [X] Implement a client that can connect to the server and send messages.
* [ ] Test the server by connecting multiple clients and sending messages.
* [ ] Implement error handling and graceful shutdown of the server.

### My Improvment

* [ ] Adding ID to any connected client
* [ ] Adding timestamp for every incoming message
* [ ] Making sure when client send a message other client recieve it immediately
* [ ] Implement message when client dissconect
