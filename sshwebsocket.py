import asyncio
import paramiko
import websockets
import os
import pty
import select

SSH_HOST = "192.168.100.18"
SSH_USER = "minitel"
SSH_PORT = 22

async def handler(ws):
    # --- SSH ---
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
    SSH_HOST,
    port=SSH_PORT,
    username=SSH_USER,
    password="lol"
)

    chan = client.invoke_shell(
        term='m1b',
        width=40,
        height=24
    )

    chan.send("stty -ixon\n")

    async def ws_to_ssh():
        async for msg in ws:
            if isinstance(msg, str):
                chan.send(msg.encode("latin1", errors="ignore").decode("latin1"))
            else:
                chan.send(msg.decode("latin1", errors="ignore"))

    async def ssh_to_ws():
        while True:
            if chan.recv_ready():
                data = chan.recv(1024)
                await ws.send(data.decode("latin1", errors="ignore"))
            await asyncio.sleep(0.01)

    await asyncio.gather(ws_to_ssh(), ssh_to_ws())

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("Passerelle SSH–Minitel prête")
        await asyncio.Future()

asyncio.run(main())
