# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/gnss/proto/gnss.proto

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
  name='modules/drivers/gnss/proto/gnss.proto',
  package='apollo.drivers.gnss',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n%modules/drivers/gnss/proto/gnss.proto\x12\x13\x61pollo.drivers.gnss\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto\"\x82\x04\n\x04Gnss\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x18\n\x10measurement_time\x18\x02 \x01(\x01\x12\x1b\n\x10velocity_latency\x18\x03 \x01(\x02:\x01\x30\x12)\n\x08position\x18\x04 \x01(\x0b\x32\x17.apollo.common.PointLLH\x12\x30\n\x10position_std_dev\x18\x05 \x01(\x0b\x32\x16.apollo.common.Point3D\x12/\n\x0flinear_velocity\x18\x06 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x37\n\x17linear_velocity_std_dev\x18\x07 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x10\n\x08num_sats\x18\x08 \x01(\x05\x12,\n\x04type\x18\t \x01(\x0e\x32\x1e.apollo.drivers.gnss.Gnss.Type\x12\x17\n\x0fsolution_status\x18\n \x01(\r\x12\x15\n\rposition_type\x18\x0b \x01(\r\"e\n\x04Type\x12\x0b\n\x07INVALID\x10\x00\x12\x0e\n\nPROPAGATED\x10\x01\x12\n\n\x06SINGLE\x10\x02\x12\x0b\n\x07PSRDIFF\x10\x03\x12\x07\n\x03PPP\x10\x04\x12\r\n\tRTK_FLOAT\x10\x05\x12\x0f\n\x0bRTK_INTEGER\x10\x06\">\n\x07RawData\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,modules_dot_common_dot_proto_dot_geometry__pb2.DESCRIPTOR,])



_GNSS_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='apollo.drivers.gnss.Gnss.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPAGATED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SINGLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PSRDIFF', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PPP', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTK_FLOAT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTK_INTEGER', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=548,
  serialized_end=649,
)
_sym_db.RegisterEnumDescriptor(_GNSS_TYPE)


_GNSS = _descriptor.Descriptor(
  name='Gnss',
  full_name='apollo.drivers.gnss.Gnss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.drivers.gnss.Gnss.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measurement_time', full_name='apollo.drivers.gnss.Gnss.measurement_time', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity_latency', full_name='apollo.drivers.gnss.Gnss.velocity_latency', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='apollo.drivers.gnss.Gnss.position', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position_std_dev', full_name='apollo.drivers.gnss.Gnss.position_std_dev', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear_velocity', full_name='apollo.drivers.gnss.Gnss.linear_velocity', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear_velocity_std_dev', full_name='apollo.drivers.gnss.Gnss.linear_velocity_std_dev', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_sats', full_name='apollo.drivers.gnss.Gnss.num_sats', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='apollo.drivers.gnss.Gnss.type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='solution_status', full_name='apollo.drivers.gnss.Gnss.solution_status', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position_type', full_name='apollo.drivers.gnss.Gnss.position_type', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GNSS_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=649,
)


_RAWDATA = _descriptor.Descriptor(
  name='RawData',
  full_name='apollo.drivers.gnss.RawData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.drivers.gnss.RawData.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='apollo.drivers.gnss.RawData.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=651,
  serialized_end=713,
)

_GNSS.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_GNSS.fields_by_name['position'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINTLLH
_GNSS.fields_by_name['position_std_dev'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_GNSS.fields_by_name['linear_velocity'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_GNSS.fields_by_name['linear_velocity_std_dev'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_GNSS.fields_by_name['type'].enum_type = _GNSS_TYPE
_GNSS_TYPE.containing_type = _GNSS
_RAWDATA.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
DESCRIPTOR.message_types_by_name['Gnss'] = _GNSS
DESCRIPTOR.message_types_by_name['RawData'] = _RAWDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Gnss = _reflection.GeneratedProtocolMessageType('Gnss', (_message.Message,), dict(
  DESCRIPTOR = _GNSS,
  __module__ = 'modules.drivers.gnss.proto.gnss_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.Gnss)
  ))
_sym_db.RegisterMessage(Gnss)

RawData = _reflection.GeneratedProtocolMessageType('RawData', (_message.Message,), dict(
  DESCRIPTOR = _RAWDATA,
  __module__ = 'modules.drivers.gnss.proto.gnss_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.RawData)
  ))
_sym_db.RegisterMessage(RawData)


# @@protoc_insertion_point(module_scope)
