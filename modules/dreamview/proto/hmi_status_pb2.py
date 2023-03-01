# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/dreamview/proto/hmi_status.proto

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
from modules.monitor.proto import \
    system_status_pb2 as modules_dot_monitor_dot_proto_dot_system__status__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/dreamview/proto/hmi_status.proto',
  package='apollo.dreamview',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n(modules/dreamview/proto/hmi_status.proto\x12\x10\x61pollo.dreamview\x1a!modules/common/proto/header.proto\x1a)modules/monitor/proto/system_status.proto\"\xa8\x05\n\tHMIStatus\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\r\n\x05modes\x18\x02 \x03(\t\x12\x14\n\x0c\x63urrent_mode\x18\x03 \x01(\t\x12\x0c\n\x04maps\x18\x04 \x03(\t\x12\x13\n\x0b\x63urrent_map\x18\x05 \x01(\t\x12\x10\n\x08vehicles\x18\x06 \x03(\t\x12\x17\n\x0f\x63urrent_vehicle\x18\x07 \x01(\t\x12\x39\n\x07modules\x18\x08 \x03(\x0b\x32(.apollo.dreamview.HMIStatus.ModulesEntry\x12R\n\x14monitored_components\x18\t \x03(\x0b\x32\x34.apollo.dreamview.HMIStatus.MonitoredComponentsEntry\x12\x14\n\x0c\x64ocker_image\x18\n \x01(\t\x12\x13\n\x0butm_zone_id\x18\x0b \x01(\x05\x12\x15\n\rpassenger_msg\x18\x0c \x01(\t\x12J\n\x10other_components\x18\r \x03(\x0b\x32\x30.apollo.dreamview.HMIStatus.OtherComponentsEntry\x1a.\n\x0cModulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a[\n\x18MonitoredComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.apollo.monitor.ComponentStatus:\x02\x38\x01\x1aW\n\x14OtherComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.apollo.monitor.ComponentStatus:\x02\x38\x01')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,modules_dot_monitor_dot_proto_dot_system__status__pb2.DESCRIPTOR,])




_HMISTATUS_MODULESENTRY = _descriptor.Descriptor(
  name='ModulesEntry',
  full_name='apollo.dreamview.HMIStatus.ModulesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='apollo.dreamview.HMIStatus.ModulesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='apollo.dreamview.HMIStatus.ModulesEntry.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=593,
  serialized_end=639,
)

_HMISTATUS_MONITOREDCOMPONENTSENTRY = _descriptor.Descriptor(
  name='MonitoredComponentsEntry',
  full_name='apollo.dreamview.HMIStatus.MonitoredComponentsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='apollo.dreamview.HMIStatus.MonitoredComponentsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='apollo.dreamview.HMIStatus.MonitoredComponentsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=641,
  serialized_end=732,
)

_HMISTATUS_OTHERCOMPONENTSENTRY = _descriptor.Descriptor(
  name='OtherComponentsEntry',
  full_name='apollo.dreamview.HMIStatus.OtherComponentsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='apollo.dreamview.HMIStatus.OtherComponentsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='apollo.dreamview.HMIStatus.OtherComponentsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=734,
  serialized_end=821,
)

_HMISTATUS = _descriptor.Descriptor(
  name='HMIStatus',
  full_name='apollo.dreamview.HMIStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.dreamview.HMIStatus.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modes', full_name='apollo.dreamview.HMIStatus.modes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_mode', full_name='apollo.dreamview.HMIStatus.current_mode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maps', full_name='apollo.dreamview.HMIStatus.maps', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_map', full_name='apollo.dreamview.HMIStatus.current_map', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vehicles', full_name='apollo.dreamview.HMIStatus.vehicles', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_vehicle', full_name='apollo.dreamview.HMIStatus.current_vehicle', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modules', full_name='apollo.dreamview.HMIStatus.modules', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='monitored_components', full_name='apollo.dreamview.HMIStatus.monitored_components', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='docker_image', full_name='apollo.dreamview.HMIStatus.docker_image', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='utm_zone_id', full_name='apollo.dreamview.HMIStatus.utm_zone_id', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passenger_msg', full_name='apollo.dreamview.HMIStatus.passenger_msg', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_components', full_name='apollo.dreamview.HMIStatus.other_components', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HMISTATUS_MODULESENTRY, _HMISTATUS_MONITOREDCOMPONENTSENTRY, _HMISTATUS_OTHERCOMPONENTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=821,
)

_HMISTATUS_MODULESENTRY.containing_type = _HMISTATUS
_HMISTATUS_MONITOREDCOMPONENTSENTRY.fields_by_name['value'].message_type = modules_dot_monitor_dot_proto_dot_system__status__pb2._COMPONENTSTATUS
_HMISTATUS_MONITOREDCOMPONENTSENTRY.containing_type = _HMISTATUS
_HMISTATUS_OTHERCOMPONENTSENTRY.fields_by_name['value'].message_type = modules_dot_monitor_dot_proto_dot_system__status__pb2._COMPONENTSTATUS
_HMISTATUS_OTHERCOMPONENTSENTRY.containing_type = _HMISTATUS
_HMISTATUS.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_HMISTATUS.fields_by_name['modules'].message_type = _HMISTATUS_MODULESENTRY
_HMISTATUS.fields_by_name['monitored_components'].message_type = _HMISTATUS_MONITOREDCOMPONENTSENTRY
_HMISTATUS.fields_by_name['other_components'].message_type = _HMISTATUS_OTHERCOMPONENTSENTRY
DESCRIPTOR.message_types_by_name['HMIStatus'] = _HMISTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HMIStatus = _reflection.GeneratedProtocolMessageType('HMIStatus', (_message.Message,), dict(

  ModulesEntry = _reflection.GeneratedProtocolMessageType('ModulesEntry', (_message.Message,), dict(
    DESCRIPTOR = _HMISTATUS_MODULESENTRY,
    __module__ = 'modules.dreamview.proto.hmi_status_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIStatus.ModulesEntry)
    ))
  ,

  MonitoredComponentsEntry = _reflection.GeneratedProtocolMessageType('MonitoredComponentsEntry', (_message.Message,), dict(
    DESCRIPTOR = _HMISTATUS_MONITOREDCOMPONENTSENTRY,
    __module__ = 'modules.dreamview.proto.hmi_status_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIStatus.MonitoredComponentsEntry)
    ))
  ,

  OtherComponentsEntry = _reflection.GeneratedProtocolMessageType('OtherComponentsEntry', (_message.Message,), dict(
    DESCRIPTOR = _HMISTATUS_OTHERCOMPONENTSENTRY,
    __module__ = 'modules.dreamview.proto.hmi_status_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIStatus.OtherComponentsEntry)
    ))
  ,
  DESCRIPTOR = _HMISTATUS,
  __module__ = 'modules.dreamview.proto.hmi_status_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIStatus)
  ))
_sym_db.RegisterMessage(HMIStatus)
_sym_db.RegisterMessage(HMIStatus.ModulesEntry)
_sym_db.RegisterMessage(HMIStatus.MonitoredComponentsEntry)
_sym_db.RegisterMessage(HMIStatus.OtherComponentsEntry)


_HMISTATUS_MODULESENTRY._options = None
_HMISTATUS_MONITOREDCOMPONENTSENTRY._options = None
_HMISTATUS_OTHERCOMPONENTSENTRY._options = None
# @@protoc_insertion_point(module_scope)
