# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common/util/testdata/simple.proto

import sys

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.common.proto import \
    header_pb2 as modules_dot_common_dot_proto_dot_header__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/common/util/testdata/simple.proto',
  package='apollo.common.util.test',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n)modules/common/util/testdata/simple.proto\x12\x17\x61pollo.common.util.test\x1a!modules/common/proto/header.proto\"U\n\rSimpleMessage\x12\x0f\n\x07integer\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\x12%\n\x06header\x18\x03 \x01(\x0b\x32\x15.apollo.common.Header\"P\n\x15SimpleRepeatedMessage\x12\x37\n\x07message\x18\x01 \x03(\x0b\x32&.apollo.common.util.test.SimpleMessage')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,])




_SIMPLEMESSAGE = _descriptor.Descriptor(
  name='SimpleMessage',
  full_name='apollo.common.util.test.SimpleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='integer', full_name='apollo.common.util.test.SimpleMessage.integer', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='apollo.common.util.test.SimpleMessage.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.common.util.test.SimpleMessage.header', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=105,
  serialized_end=190,
)


_SIMPLEREPEATEDMESSAGE = _descriptor.Descriptor(
  name='SimpleRepeatedMessage',
  full_name='apollo.common.util.test.SimpleRepeatedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='apollo.common.util.test.SimpleRepeatedMessage.message', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=192,
  serialized_end=272,
)

_SIMPLEMESSAGE.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_SIMPLEREPEATEDMESSAGE.fields_by_name['message'].message_type = _SIMPLEMESSAGE
DESCRIPTOR.message_types_by_name['SimpleMessage'] = _SIMPLEMESSAGE
DESCRIPTOR.message_types_by_name['SimpleRepeatedMessage'] = _SIMPLEREPEATEDMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleMessage = _reflection.GeneratedProtocolMessageType('SimpleMessage', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLEMESSAGE,
  __module__ = 'modules.common.util.testdata.simple_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.util.test.SimpleMessage)
  ))
_sym_db.RegisterMessage(SimpleMessage)

SimpleRepeatedMessage = _reflection.GeneratedProtocolMessageType('SimpleRepeatedMessage', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLEREPEATEDMESSAGE,
  __module__ = 'modules.common.util.testdata.simple_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.util.test.SimpleRepeatedMessage)
  ))
_sym_db.RegisterMessage(SimpleRepeatedMessage)


# @@protoc_insertion_point(module_scope)
