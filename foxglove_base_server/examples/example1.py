import os
import threading
from types import ModuleType
from foxglove_base_msgs.msgs import FloatMsg_pb2
from base64 import standard_b64encode
from foxglove_websocket import run_cancellable
from foxglove_base_server.server import FoxgloveServerHandler
from foxglove_base_server.channel import Channel
from foxglove_base_server.msg import Msg

def get_schema(msg_module: ModuleType, msg_bin: str):
    with open(os.path.join(os.path.dirname(msg_module.__file__), msg_bin), "rb") as schema_bin:
        return standard_b64encode(schema_bin.read()).decode("ascii")
    
def main():
    server_handler = FoxgloveServerHandler()
    msg = Msg(FloatMsg_pb2.FloatMsg(data=10.0), Channel("test_msg", "protobuf", "FloatMsg", get_schema(FloatMsg_pb2, "FloatMsg.bin")))
    server_handler.add_msg(msg)
    thread = threading.Thread(target=run_cancellable(server_handler.start_server()), args=(server_handler,))

if __name__ == "__main__":
    main()