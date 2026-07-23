# Roadmap.sh Broadcast Server

### What I am Gonna Learn

* Websockets
* Real Time Communication

### Requirements

* [ ] Implement 'broadcast-server start' for starting the server
* [ ] Implement 'broadcast-server connect' for connecting the client to server
* [X] Listen at spesified port(either configure using command or hardcoded)
* [X] Handling multiple client
* [X] Proper disconnect

### Implementation

* [X] Create a server that listens for incoming connections.
* [X] When a client connects, store the connection in a list of connected clients.
* [X] When a client sends a message, broadcast this message to all connected clients.
* [ ] Handle client disconnections and remove the client from the list of connected clients.
* [X] Implement a client that can connect to the server and send messages.
* [X] Test the server by connecting multiple clients and sending messages.
* [X] Implement error handling and graceful shutdown of the server.

### My Improvment

* [X] Adding ID to any connected client
* [X] Adding datetime for every incoming message
* [X] Making sure when client send a message other client recieve it immediately
* [X] Implement message when client dissconect
* [X] Allow user to set their username



### Installation

* Clone this project and install asioconsole package first since everything else is already supported on the newer version of Python

```Python
pip install aioconsole
```


### How To Use

* Run the server script first

```Python
python server.py
```

* Then run the client script

```Python
python client.py
```

* Enter your desired name in the client side

```
Enter Your name:
```

* Once you entered the name in the client, you'll see the update in the server side like this

```
Client with uuid [insert uuid here] has been registerd as [your name]
```

* Type the message in the client side and send it using enter
* The server side will recieve the message from the client side
