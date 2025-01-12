import unittest

from socketio import msgpack_packet
from socketio import packet


class TestMsgPackPacket(unittest.TestCase):
    def test_encode_decode(self):
        p = msgpack_packet.MsgPackPacket(
            packet.CONNECT, data={'auth': {'token': '123'}}, namespace='/foo')
        p2 = msgpack_packet.MsgPackPacket(encoded_packet=p.encode())
        assert p.packet_type == p2.packet_type
        assert p.data == p2.data
        assert p.id == p2.id
        assert p.namespace == p2.namespace

    def test_encode_decode_with_id(self):
        p = msgpack_packet.MsgPackPacket(
            packet.EVENT, data=['ev', 42], id=123, namespace='/foo')
        p2 = msgpack_packet.MsgPackPacket(encoded_packet=p.encode())
        assert p.packet_type == p2.packet_type
        assert p.data == p2.data
        assert p.id == p2.id
        assert p.namespace == p2.namespace
