import asyncio
import websockets
import datetime

datenow = datetime.datetime.now()

async def chat():
    async with websockets.connect('ws://localhost:6767') as websocket:
        while True:
            message = input('Enter message: ')
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Received at {datenow} :{response}")

if __name__ == "__main__":
    asyncio.run(chat())