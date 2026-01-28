import asyncio
import websockets
import uuid
import datetime

connected_clients  = set() #initialize set for list of connected client
client_uuids = {} #initialize dictionary for uuid
datenow = datetime.datetime.now()

async def handle_client(websocket): #handle client connection
    client_id = uuid.uuid4() #implement uuid v4
    connected_clients.add(websocket) #add connected client to the set
    client_uuids[websocket] = client_id #set uuid for each connected client
    try:
        async for message in websocket: #listen messages
            for client in connected_clients: #broadcaset messages
                await client.send(message)
                print(f"Received at {datenow} by client {client_uuids[websocket]} : {message}")
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        print(f"Client {client_uuids[websocket]} has been disconnected")
        connected_clients.remove(websocket) #remove the client
        #show message that a client has been disconnect
        del client_uuids[websocket]

async def main():
    server = await websockets.serve(handle_client,'localhost',6767,ping_interval=None)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())