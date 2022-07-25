# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/v2x/proto/v2x_obu_rsi.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/v2x/proto/v2x_obu_rsi.proto',
  package='apollo.v2x.obu',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n#modules/v2x/proto/v2x_obu_rsi.proto\x12\x0e\x61pollo.v2x.obu\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto\"\xec\x01\n\x06ObuRsi\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x0e\n\x06rsu_id\x18\x02 \x01(\x0c\x12\x0e\n\x06rsi_id\x18\x03 \x01(\x05\x12\x12\n\nalter_type\x18\x04 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12)\n\tref_point\x18\x06 \x01(\x0b\x32\x16.apollo.common.Point2D\x12&\n\x06points\x18\x07 \x03(\x0b\x32\x16.apollo.common.Point2D\x12\x0e\n\x06radius\x18\x08 \x01(\x05\x12\x0f\n\x07msg_cnt\x18\t \x01(\x05')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,modules_dot_common_dot_proto_dot_geometry__pb2.DESCRIPTOR,])




_OBURSI = _descriptor.Descriptor(
  name='ObuRsi',
  full_name='apollo.v2x.obu.ObuRsi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.v2x.obu.ObuRsi.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rsu_id', full_name='apollo.v2x.obu.ObuRsi.rsu_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rsi_id', full_name='apollo.v2x.obu.ObuRsi.rsi_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alter_type', full_name='apollo.v2x.obu.ObuRsi.alter_type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='apollo.v2x.obu.ObuRsi.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref_point', full_name='apollo.v2x.obu.ObuRsi.ref_point', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='points', full_name='apollo.v2x.obu.ObuRsi.points', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius', full_name='apollo.v2x.obu.ObuRsi.radius', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_cnt', full_name='apollo.v2x.obu.ObuRsi.msg_cnt', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=364,
)

_OBURSI.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_OBURSI.fields_by_name['ref_point'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT2D
_OBURSI.fields_by_name['points'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT2D
DESCRIPTOR.message_types_by_name['ObuRsi'] = _OBURSI
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObuRsi = _reflection.GeneratedProtocolMessageType('ObuRsi', (_message.Message,), dict(
  DESCRIPTOR = _OBURSI,
  __module__ = 'modules.v2x.proto.v2x_obu_rsi_pb2'
  # @@protoc_insertion_point(class_scope:apollo.v2x.obu.ObuRsi)
  ))
_sym_db.RegisterMessage(ObuRsi)


# @@protoc_insertion_point(module_scope)
