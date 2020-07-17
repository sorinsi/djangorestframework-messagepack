import unittest

from datetime import datetime
from io import BytesIO
from uuid import uuid4

from rest_framework.serializers import DateTimeField, DateField, UUIDField, TimeField, Serializer

from rest_framework_messagepack.parsers import MessagePackParser
from rest_framework_messagepack.renderers import MessagePackRenderer


class TestRenderParser(unittest.TestCase):
    """
        Tests renderer and the output from the renderer will test the parser.
    """

    def test_renderer_and_parser(self):
        """
            With this method we render and parse data using special cases where MessagePack may fail.
        :return:
        """
        # Input, Output
        self.field_tests = (
            (datetime.now(), DateTimeField),
            (datetime.now().date(), DateField),
            (uuid4(), UUIDField),
            (datetime.now().time(), TimeField)
        )

        renderer = MessagePackRenderer()
        parser = MessagePackParser()

        for field_test in self.field_tests:
            data = field_test[0]
            field_type = field_test[1]

            # We need to create a Serializer with the field needed dynamically
            # in order to test if our render/parser works correctly.
            cls = type("TestClassDynamic", (Serializer, ), {"field": field_type()})

            to_message_pack = renderer.render(data)
            from_message_pack = parser.parse(BytesIO(to_message_pack))

            serializer = cls(data={"field": from_message_pack})

            # Tests will fail if this crashes
            serializer.is_valid(raise_exception=True)
