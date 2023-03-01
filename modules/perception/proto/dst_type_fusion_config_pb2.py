# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/proto/dst_type_fusion_config.proto

import sys

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/perception/proto/dst_type_fusion_config.proto',
  package='apollo.perception.fusion',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n5modules/perception/proto/dst_type_fusion_config.proto\x12\x18\x61pollo.perception.fusion\"}\n\x18\x43\x61meraDstTypeFusionParam\x12\x0e\n\x04name\x18\x01 \x01(\t:\x00\x12\x15\n\nvalid_dist\x18\x02 \x01(\x01:\x01\x30\x12\x16\n\x0breliability\x18\x03 \x01(\x01:\x01\x30\x12\"\n\x17reliability_for_unknown\x18\x04 \x01(\x01:\x01\x30\"e\n\x17LidarDstTypeFusionParam\x12\x0e\n\x04name\x18\x01 \x01(\t:\x00\x12\x16\n\x0breliability\x18\x02 \x01(\x01:\x01\x30\x12\"\n\x17reliability_for_unknown\x18\x03 \x01(\x01:\x01\x30\"\xa9\x01\n\x13\x44stTypeFusionConfig\x12I\n\rcamera_params\x18\x01 \x03(\x0b\x32\x32.apollo.perception.fusion.CameraDstTypeFusionParam\x12G\n\x0clidar_params\x18\x02 \x03(\x0b\x32\x31.apollo.perception.fusion.LidarDstTypeFusionParam')
)




_CAMERADSTTYPEFUSIONPARAM = _descriptor.Descriptor(
  name='CameraDstTypeFusionParam',
  full_name='apollo.perception.fusion.CameraDstTypeFusionParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='apollo.perception.fusion.CameraDstTypeFusionParam.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid_dist', full_name='apollo.perception.fusion.CameraDstTypeFusionParam.valid_dist', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reliability', full_name='apollo.perception.fusion.CameraDstTypeFusionParam.reliability', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reliability_for_unknown', full_name='apollo.perception.fusion.CameraDstTypeFusionParam.reliability_for_unknown', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
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
  serialized_start=83,
  serialized_end=208,
)


_LIDARDSTTYPEFUSIONPARAM = _descriptor.Descriptor(
  name='LidarDstTypeFusionParam',
  full_name='apollo.perception.fusion.LidarDstTypeFusionParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='apollo.perception.fusion.LidarDstTypeFusionParam.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reliability', full_name='apollo.perception.fusion.LidarDstTypeFusionParam.reliability', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reliability_for_unknown', full_name='apollo.perception.fusion.LidarDstTypeFusionParam.reliability_for_unknown', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
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
  serialized_start=210,
  serialized_end=311,
)


_DSTTYPEFUSIONCONFIG = _descriptor.Descriptor(
  name='DstTypeFusionConfig',
  full_name='apollo.perception.fusion.DstTypeFusionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='camera_params', full_name='apollo.perception.fusion.DstTypeFusionConfig.camera_params', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lidar_params', full_name='apollo.perception.fusion.DstTypeFusionConfig.lidar_params', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=314,
  serialized_end=483,
)

_DSTTYPEFUSIONCONFIG.fields_by_name['camera_params'].message_type = _CAMERADSTTYPEFUSIONPARAM
_DSTTYPEFUSIONCONFIG.fields_by_name['lidar_params'].message_type = _LIDARDSTTYPEFUSIONPARAM
DESCRIPTOR.message_types_by_name['CameraDstTypeFusionParam'] = _CAMERADSTTYPEFUSIONPARAM
DESCRIPTOR.message_types_by_name['LidarDstTypeFusionParam'] = _LIDARDSTTYPEFUSIONPARAM
DESCRIPTOR.message_types_by_name['DstTypeFusionConfig'] = _DSTTYPEFUSIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CameraDstTypeFusionParam = _reflection.GeneratedProtocolMessageType('CameraDstTypeFusionParam', (_message.Message,), dict(
  DESCRIPTOR = _CAMERADSTTYPEFUSIONPARAM,
  __module__ = 'modules.perception.proto.dst_type_fusion_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.fusion.CameraDstTypeFusionParam)
  ))
_sym_db.RegisterMessage(CameraDstTypeFusionParam)

LidarDstTypeFusionParam = _reflection.GeneratedProtocolMessageType('LidarDstTypeFusionParam', (_message.Message,), dict(
  DESCRIPTOR = _LIDARDSTTYPEFUSIONPARAM,
  __module__ = 'modules.perception.proto.dst_type_fusion_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.fusion.LidarDstTypeFusionParam)
  ))
_sym_db.RegisterMessage(LidarDstTypeFusionParam)

DstTypeFusionConfig = _reflection.GeneratedProtocolMessageType('DstTypeFusionConfig', (_message.Message,), dict(
  DESCRIPTOR = _DSTTYPEFUSIONCONFIG,
  __module__ = 'modules.perception.proto.dst_type_fusion_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.fusion.DstTypeFusionConfig)
  ))
_sym_db.RegisterMessage(DstTypeFusionConfig)


# @@protoc_insertion_point(module_scope)
