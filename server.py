import os
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn

app = FastAPI(title="All Super VPN", version="1.0.0")


@app.get("/")
def read_root():
  return {
      "app_name": "All Super VPN",
      "status": "Online & Blazing Fast",
      "message": (
          "Welcome to All Super VPN! Your private high-speed tunnel is active."
      ),
  }


@app.websocket("/connect")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  print("[All Super VPN] New client connected securely!")
  try:
    while True:
      data = await websocket.receive_bytes()
      response_data = data
      await websocket.send_bytes(response_data)
  except WebSocketDisconnect:
    print("[All Super VPN] Client disconnected.")


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 8000))
  uvicorn.run(app, host="0.0.0.0", port=port)
