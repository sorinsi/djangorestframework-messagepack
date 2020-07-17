import msgpack
from rest_framework.renderers import BaseRenderer

from rest_framework_messagepack.encoders import MessagePackEncoder


class MessagePackRenderer(BaseRenderer):
    media_type = "application/msgpack"
    format = "msgpack"
    render_style = "binary"
    encoder_class = MessagePackEncoder

    def render(self, data, *args, **kwargs):
        if data is None:
            return b""

        # Custom encoder is used in order to be able to deal with
        # types like datetime and others.
        return msgpack.dumps(data, default=self.encoder_class.encode)
