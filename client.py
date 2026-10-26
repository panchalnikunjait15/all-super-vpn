import asyncio
import websockets

SERVER_URI = "wss://vajra-vpn.onrender.com/connect"


async def run_client():
  print("=" * 40)
  print("       ALL SUPER VPN - CLIENT       ")
  print("=" * 40)
  print(f"Connecting to All Super VPN Server...")

  try:
    async with websockets.connect(SERVER_URI) as websocket:
      print(
          "[✓] Connected successfully to All Super VPN! Tunnel is 100% active."
      )
      print(
          "Type your message/data to send through the tunnel (Type 'exit' to"
          " quit):\n"
      )

      while True:
        message = input("All Super VPN > ")
        if message.lower() == "exit":
          print("Closing All Super VPN connection...")
          break

        await websocket.send(message.encode("utf-8"))
        response = await websocket.recv()
        print(f"[Server Response]: {response}\n")

  except Exception as e:
    print(f"[!] Connection Error: {e}")


if __name__ == "__main__":
  asyncio.run(run_client())
