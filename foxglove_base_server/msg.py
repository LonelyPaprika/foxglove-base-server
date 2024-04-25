from .channel import Channel

class Msg:
    def __init__(self, msg, channel: Channel):
        self._msg = msg
        self._channel = channel

    @property
    def msg(self):
        return self._msg
    
    @msg.setter
    def msg(self, new_msg):
        self._msg = new_msg
    
    @property
    def channel(self):
        return self._channel
        