
import asyncio
import time
from foxglove_websocket.server import FoxgloveServer
from msg import Msg
from typing import List

class FoxgloveServerHandler:
    def __init__(self, address="0.0.0.0", port=8765, server_name="example server"):
        self.address = address
        self.port = port
        self.server_name = server_name
        self.value = 0
        self.msgs: List[Msg] = []

    def add_msg(self, msg: Msg):
        self.msgs.append(msg)

    def update_msg(self, msg: Msg):
        for (idx, m) in enumerate(self.msgs):
            if m.channel.topic == msg.channel.topic:
                self.msgs[idx] = m

    async def load_channel(self, server):
        for msg in self.msgs:
            msg.channel.chn_id = await server.add_channel(
                {
                    "topic": msg.channel.topic,
                    "encoding": msg.channel.encoding,
                    "schemaName": msg.channel.schema_name,
                    "schema": msg.channel.schema,
                }
            )
            
    async def start_server(self):
        async with FoxgloveServer(self.address, self.port, self.server_name) as server:            
            await self.load_channel(server)
            await self.send_messages(server)

    async def send_messages(self, server):
        while True:
            await asyncio.sleep(0.2)
            for msg in self.msgs:
                await self.send_message(msg, server)

    async def send_message(self, msg: Msg, server):
        await server.send_message(
            msg.channel.chn_id,
            time.time_ns(),
            msg.msg.SerializeToString(),
        )