import asyncio
import websockets
from datetime import datetime
uri = "ws://localhost:8000"
name = 'clientname'
def sendtext(msg):
    asyncio.get_event_loop().run_until_complete(sendmsg(msg))
async def sendmsg(msg):
    message = msg
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)
    async with websockets.connect(uri) as websocket:
        await websocket.send(f'{dt_string}~~{name}~~{message}')
        x = await websocket.recv()
        

