import asyncio
import websockets
import base64 , json , os 

# Path to your image file (replace with your actual image file)
image_path = None
with open(os.path.join(os.path.dirname(__file__),"shared_data.json")) as buff : image_path = json.load(buff)['img']

async def handle_websocket(websocket, path):
	while True:
		message = "This is a real-time message from the server!"
		with open(image_path, "rb") as img_file:
			image_data = base64.b64encode(img_file.read()).decode('utf-8')
			await websocket.send(image_data)
		print(message)
		await asyncio.sleep(1)  # Send a message every second

start_server = websockets.serve(handle_websocket, 'localhost', 8765)  # Replace with your desired host and port
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()