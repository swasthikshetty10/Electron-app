from asyncio.events import get_event_loop
import asyncio
import websockets
import json


  
async def echo(websocket, path):
    async for message in websocket:
        data = message.split('~~')
        print(data)
        
        
        
            
        await websocket.send(message)
    
   
        

start_server = websockets.serve(echo, "localhost", 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()