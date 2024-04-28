class Channel:
    def __init__(self, topic: str, encoding: str, schema_name: str, schema: str):
        self._topic = topic
        self._encoding = encoding
        self._schema_name = schema_name
        self._schema = schema
        self._chn_id = None

    @property
    def topic(self):
        return self._topic

    @property
    def encoding(self):
        return self._encoding

    @property
    def schema_name(self):
        return self._schema_name

    @property
    def schema(self):
        return self._schema

    @property
    def chn_id(self):
        return self._chn_id

    @chn_id.setter
    def chn_id(self, chn_id):
        self._chn_id = chn_id
