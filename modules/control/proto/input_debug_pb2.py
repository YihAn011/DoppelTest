# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/control/proto/input_debug.proto

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
  name='modules/control/proto/input_debug.proto',
  package='apollo.control',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\'modules/control/proto/input_debug.proto\x12\x0e\x61pollo.control\x1a!modules/common/proto/header.proto\"\xe0\x01\n\nInputDebug\x12\x32\n\x13localization_header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12,\n\rcanbus_header\x18\x02 \x01(\x0b\x32\x15.apollo.common.Header\x12\x30\n\x11trajectory_header\x18\x03 \x01(\x0b\x32\x15.apollo.common.Header\x12>\n\x1flatest_replan_trajectory_header\x18\x04 \x01(\x0b\x32\x15.apollo.common.Header')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,])




_INPUTDEBUG = _descriptor.Descriptor(
  name='InputDebug',
  full_name='apollo.control.InputDebug',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='localization_header', full_name='apollo.control.InputDebug.localization_header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='canbus_header', full_name='apollo.control.InputDebug.canbus_header', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trajectory_header', full_name='apollo.control.InputDebug.trajectory_header', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latest_replan_trajectory_header', full_name='apollo.control.InputDebug.latest_replan_trajectory_header', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=95,
  serialized_end=319,
)

_INPUTDEBUG.fields_by_name['localization_header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_INPUTDEBUG.fields_by_name['canbus_header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_INPUTDEBUG.fields_by_name['trajectory_header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_INPUTDEBUG.fields_by_name['latest_replan_trajectory_header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
DESCRIPTOR.message_types_by_name['InputDebug'] = _INPUTDEBUG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputDebug = _reflection.GeneratedProtocolMessageType('InputDebug', (_message.Message,), dict(
  DESCRIPTOR = _INPUTDEBUG,
  __module__ = 'modules.control.proto.input_debug_pb2'
  # @@protoc_insertion_point(class_scope:apollo.control.InputDebug)
  ))
_sym_db.RegisterMessage(InputDebug)


# @@protoc_insertion_point(module_scope)
