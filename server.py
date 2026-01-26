import asyncio
import websockets

connected_clients  = set() #initialize set for list of connected client

async def handle_client(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients:
                if client is websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

    async def main():
        server = await websockets.serve(handle_client,'localhost',6767)
        await server.wait_closed()

    if __name__ == "__main__":
        asyncio.run(main())