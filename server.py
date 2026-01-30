import asyncio
import websockets
import uuid
import datetime

connected_clients  = set() #initialize set for list of connected client
client_uuids = {} #initialize dictionary for uuid
client_usernames = {}

async def handle_client(websocket): #handle client connection
    client_id = uuid.uuid4() #implement uuid v4
    client_uuids[websocket] = client_id #set uuid for each connected client
    username = await websocket.recv()
    client_usernames[websocket] = username
    print(f"Client with uuid {client_uuids[websocket]} has been registerd as {username}")
    try:
        async for message in websocket: #listen messages
            datenow = datetime.datetime.now()
            connected_clients.add(websocket) #add connected client to the set
            for client in connected_clients: #broadcast messages
                await client.send(message)
                print(f"Received at {datenow} by {username} : {message}")
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        print(f"{username} has been disconnected")
        connected_clients.remove(websocket) #remove the client
        #show message that a client has been disconnect
        del client_uuids[websocket]
        del client_usernames[websocket]

async def main():
    server = await websockets.serve(handle_client,'localhost',6767,ping_interval=None)
    await server.wait_closed()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        server_input = input("Are you sure shutting down the server? ")
        if(server_input.lower() == "yes"):
            print("Shutting Down Server")