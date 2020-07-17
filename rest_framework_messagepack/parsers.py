import msgpack
from rest_framework.exceptions import ParseError
from rest_framework.parsers import BaseParser


class MessagePackParser(BaseParser):
    media_type = "application/msgpack"

    def parse(self, stream, media_type=None, parser_context=None):
        try:
            return msgpack.load(stream)
        except Exception as exc:
            raise ParseError("MessagePack parse error - %s" % str(exc))
