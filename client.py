import asyncio
import websockets
import datetime
import aioconsole

datenow = datetime.datetime.now()

async def chat():
    async with websockets.connect('ws://localhost:6767') as websocket:
        async def send_messages():
             while True:
                  print("Enter Your Message Below")
                  message = await aioconsole.ainput()
                  await websocket.send(message) #kirimkan pesan ke server

        async def recieve_messages():
            while True:
                response = await websocket.recv()
                print(f"Received at {datenow} : {response}")

        await asyncio.gather(send_messages(), recieve_messages())

if __name__ == "__main__":
    try:
        asyncio.run(chat())
    except KeyboardInterrupt:
        client_input = input("Are you sure shutting down the client?")
        if(client_input.lower() == "yes"):
            print("Shutting Down Client")