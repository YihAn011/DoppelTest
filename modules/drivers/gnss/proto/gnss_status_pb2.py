# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/gnss/proto/gnss_status.proto

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
  name='modules/drivers/gnss/proto/gnss_status.proto',
  package='apollo.drivers.gnss',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n,modules/drivers/gnss/proto/gnss_status.proto\x12\x13\x61pollo.drivers.gnss\x1a!modules/common/proto/header.proto\"\xd2\x02\n\x0cStreamStatus\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12M\n\x0fins_stream_type\x18\x02 \x01(\x0e\x32&.apollo.drivers.gnss.StreamStatus.Type:\x0c\x44ISCONNECTED\x12P\n\x12rtk_stream_in_type\x18\x03 \x01(\x0e\x32&.apollo.drivers.gnss.StreamStatus.Type:\x0c\x44ISCONNECTED\x12Q\n\x13rtk_stream_out_type\x18\x04 \x01(\x0e\x32&.apollo.drivers.gnss.StreamStatus.Type:\x0c\x44ISCONNECTED\"\'\n\x04Type\x12\x10\n\x0c\x44ISCONNECTED\x10\x00\x12\r\n\tCONNECTED\x10\x01\"\x9d\x01\n\tInsStatus\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12:\n\x04type\x18\x02 \x01(\x0e\x32#.apollo.drivers.gnss.InsStatus.Type:\x07INVALID\"-\n\x04Type\x12\x0b\n\x07INVALID\x10\x00\x12\x0e\n\nCONVERGING\x10\x01\x12\x08\n\x04GOOD\x10\x02\"\xa1\x01\n\nGnssStatus\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12!\n\x12solution_completed\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0fsolution_status\x18\x03 \x01(\r:\x01\x30\x12\x18\n\rposition_type\x18\x04 \x01(\r:\x01\x30\x12\x13\n\x08num_sats\x18\x05 \x01(\x05:\x01\x30')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,])



_STREAMSTATUS_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='apollo.drivers.gnss.StreamStatus.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DISCONNECTED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECTED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=404,
  serialized_end=443,
)
_sym_db.RegisterEnumDescriptor(_STREAMSTATUS_TYPE)

_INSSTATUS_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='apollo.drivers.gnss.InsStatus.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONVERGING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOOD', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=558,
  serialized_end=603,
)
_sym_db.RegisterEnumDescriptor(_INSSTATUS_TYPE)


_STREAMSTATUS = _descriptor.Descriptor(
  name='StreamStatus',
  full_name='apollo.drivers.gnss.StreamStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.drivers.gnss.StreamStatus.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ins_stream_type', full_name='apollo.drivers.gnss.StreamStatus.ins_stream_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rtk_stream_in_type', full_name='apollo.drivers.gnss.StreamStatus.rtk_stream_in_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rtk_stream_out_type', full_name='apollo.drivers.gnss.StreamStatus.rtk_stream_out_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STREAMSTATUS_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=443,
)


_INSSTATUS = _descriptor.Descriptor(
  name='InsStatus',
  full_name='apollo.drivers.gnss.InsStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.drivers.gnss.InsStatus.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='apollo.drivers.gnss.InsStatus.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INSSTATUS_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=446,
  serialized_end=603,
)


_GNSSSTATUS = _descriptor.Descriptor(
  name='GnssStatus',
  full_name='apollo.drivers.gnss.GnssStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.drivers.gnss.GnssStatus.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='solution_completed', full_name='apollo.drivers.gnss.GnssStatus.solution_completed', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='solution_status', full_name='apollo.drivers.gnss.GnssStatus.solution_status', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position_type', full_name='apollo.drivers.gnss.GnssStatus.position_type', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_sats', full_name='apollo.drivers.gnss.GnssStatus.num_sats', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=606,
  serialized_end=767,
)

_STREAMSTATUS.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_STREAMSTATUS.fields_by_name['ins_stream_type'].enum_type = _STREAMSTATUS_TYPE
_STREAMSTATUS.fields_by_name['rtk_stream_in_type'].enum_type = _STREAMSTATUS_TYPE
_STREAMSTATUS.fields_by_name['rtk_stream_out_type'].enum_type = _STREAMSTATUS_TYPE
_STREAMSTATUS_TYPE.containing_type = _STREAMSTATUS
_INSSTATUS.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_INSSTATUS.fields_by_name['type'].enum_type = _INSSTATUS_TYPE
_INSSTATUS_TYPE.containing_type = _INSSTATUS
_GNSSSTATUS.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
DESCRIPTOR.message_types_by_name['StreamStatus'] = _STREAMSTATUS
DESCRIPTOR.message_types_by_name['InsStatus'] = _INSSTATUS
DESCRIPTOR.message_types_by_name['GnssStatus'] = _GNSSSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamStatus = _reflection.GeneratedProtocolMessageType('StreamStatus', (_message.Message,), dict(
  DESCRIPTOR = _STREAMSTATUS,
  __module__ = 'modules.drivers.gnss.proto.gnss_status_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.StreamStatus)
  ))
_sym_db.RegisterMessage(StreamStatus)

InsStatus = _reflection.GeneratedProtocolMessageType('InsStatus', (_message.Message,), dict(
  DESCRIPTOR = _INSSTATUS,
  __module__ = 'modules.drivers.gnss.proto.gnss_status_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.InsStatus)
  ))
_sym_db.RegisterMessage(InsStatus)

GnssStatus = _reflection.GeneratedProtocolMessageType('GnssStatus', (_message.Message,), dict(
  DESCRIPTOR = _GNSSSTATUS,
  __module__ = 'modules.drivers.gnss.proto.gnss_status_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.GnssStatus)
  ))
_sym_db.RegisterMessage(GnssStatus)


# @@protoc_insertion_point(module_scope)
