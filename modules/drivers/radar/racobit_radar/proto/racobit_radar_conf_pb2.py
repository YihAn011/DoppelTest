# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/radar/racobit_radar/proto/racobit_radar_conf.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.drivers.canbus.proto import can_card_parameter_pb2 as modules_dot_drivers_dot_canbus_dot_proto_dot_can__card__parameter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/drivers/radar/racobit_radar/proto/racobit_radar_conf.proto',
  package='apollo.drivers.racobit_radar',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\nBmodules/drivers/radar/racobit_radar/proto/racobit_radar_conf.proto\x12\x1c\x61pollo.drivers.racobit_radar\x1a\x35modules/drivers/canbus/proto/can_card_parameter.proto\"\xb6\x01\n\x07\x43\x61nConf\x12\x43\n\x12\x63\x61n_card_parameter\x18\x01 \x01(\x0b\x32\'.apollo.drivers.canbus.CANCardParameter\x12 \n\x11\x65nable_debug_mode\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\"\n\x13\x65nable_receiver_log\x18\x03 \x01(\x08:\x05\x66\x61lse\x12 \n\x11\x65nable_sender_log\x18\x04 \x01(\x08:\x05\x66\x61lse\"\xd5\x05\n\tRadarConf\x12!\n\x12max_distance_valid\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x0fsensor_id_valid\x18\x02 \x01(\x08:\x05\x66\x61lse\x12 \n\x11radar_power_valid\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x11output_type_valid\x18\x04 \x01(\x08:\x04true\x12 \n\x12send_quality_valid\x18\x05 \x01(\x08:\x04true\x12!\n\x13send_ext_info_valid\x18\x06 \x01(\x08:\x04true\x12\x1f\n\x10sort_index_valid\x18\x07 \x01(\x08:\x05\x66\x61lse\x12 \n\x12store_in_nvm_valid\x18\x08 \x01(\x08:\x04true\x12\x1f\n\x10\x63trl_relay_valid\x18\t \x01(\x08:\x05\x66\x61lse\x12!\n\x13rcs_threshold_valid\x18\n \x01(\x08:\x04true\x12\x19\n\x0cmax_distance\x18\x0b \x01(\r:\x03\x32\x34\x38\x12\x14\n\tsensor_id\x18\x0c \x01(\r:\x01\x30\x12R\n\x0boutput_type\x18\r \x01(\x0e\x32(.apollo.drivers.racobit_radar.OutputType:\x13OUTPUT_TYPE_OBJECTS\x12\x16\n\x0bradar_power\x18\x0e \x01(\r:\x01\x30\x12\x15\n\nctrl_relay\x18\x0f \x01(\r:\x01\x30\x12\x1b\n\rsend_ext_info\x18\x10 \x01(\x08:\x04true\x12\x1a\n\x0csend_quality\x18\x11 \x01(\x08:\x04true\x12\x15\n\nsort_index\x18\x12 \x01(\r:\x01\x30\x12\x17\n\x0cstore_in_nvm\x18\x13 \x01(\r:\x01\x31\x12Y\n\rrcs_threshold\x18\x14 \x01(\x0e\x32*.apollo.drivers.racobit_radar.RcsThreshold:\x16RCS_THRESHOLD_STANDARD\"\x88\x01\n\x10RacobitRadarConf\x12\x37\n\x08\x63\x61n_conf\x18\x01 \x01(\x0b\x32%.apollo.drivers.racobit_radar.CanConf\x12;\n\nradar_conf\x18\x02 \x01(\x0b\x32\'.apollo.drivers.racobit_radar.RadarConf*l\n\nOutputType\x12\x14\n\x10OUTPUT_TYPE_NONE\x10\x00\x12\x17\n\x13OUTPUT_TYPE_OBJECTS\x10\x01\x12\x18\n\x14OUTPUT_TYPE_CLUSTERS\x10\x02\x12\x15\n\x11OUTPUT_TYPE_ERROR\x10\x03*g\n\x0cRcsThreshold\x12\x1a\n\x16RCS_THRESHOLD_STANDARD\x10\x00\x12\"\n\x1eRCS_THRESHOLD_HIGH_SENSITIVITY\x10\x01\x12\x17\n\x13RCS_THRESHOLD_ERROR\x10\x02')
  ,
  dependencies=[modules_dot_drivers_dot_canbus_dot_proto_dot_can__card__parameter__pb2.DESCRIPTOR,])

_OUTPUTTYPE = _descriptor.EnumDescriptor(
  name='OutputType',
  full_name='apollo.drivers.racobit_radar.OutputType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OUTPUT_TYPE_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUTPUT_TYPE_OBJECTS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUTPUT_TYPE_CLUSTERS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUTPUT_TYPE_ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1207,
  serialized_end=1315,
)
_sym_db.RegisterEnumDescriptor(_OUTPUTTYPE)

OutputType = enum_type_wrapper.EnumTypeWrapper(_OUTPUTTYPE)
_RCSTHRESHOLD = _descriptor.EnumDescriptor(
  name='RcsThreshold',
  full_name='apollo.drivers.racobit_radar.RcsThreshold',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RCS_THRESHOLD_STANDARD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RCS_THRESHOLD_HIGH_SENSITIVITY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RCS_THRESHOLD_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1317,
  serialized_end=1420,
)
_sym_db.RegisterEnumDescriptor(_RCSTHRESHOLD)

RcsThreshold = enum_type_wrapper.EnumTypeWrapper(_RCSTHRESHOLD)
OUTPUT_TYPE_NONE = 0
OUTPUT_TYPE_OBJECTS = 1
OUTPUT_TYPE_CLUSTERS = 2
OUTPUT_TYPE_ERROR = 3
RCS_THRESHOLD_STANDARD = 0
RCS_THRESHOLD_HIGH_SENSITIVITY = 1
RCS_THRESHOLD_ERROR = 2



_CANCONF = _descriptor.Descriptor(
  name='CanConf',
  full_name='apollo.drivers.racobit_radar.CanConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='can_card_parameter', full_name='apollo.drivers.racobit_radar.CanConf.can_card_parameter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_debug_mode', full_name='apollo.drivers.racobit_radar.CanConf.enable_debug_mode', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_receiver_log', full_name='apollo.drivers.racobit_radar.CanConf.enable_receiver_log', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_sender_log', full_name='apollo.drivers.racobit_radar.CanConf.enable_sender_log', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=156,
  serialized_end=338,
)


_RADARCONF = _descriptor.Descriptor(
  name='RadarConf',
  full_name='apollo.drivers.racobit_radar.RadarConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_distance_valid', full_name='apollo.drivers.racobit_radar.RadarConf.max_distance_valid', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensor_id_valid', full_name='apollo.drivers.racobit_radar.RadarConf.sensor_id_valid', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radar_power_valid', full_name='apollo.drivers.racobit_radar.RadarConf.radar_power_valid', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_type_valid', full_name='apollo.drivers.racobit_radar.RadarConf.output_type_valid', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='send_quality_valid', full_name='apollo.drivers.racobit_radar.RadarConf.send_quality_valid', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='send_ext_info_valid', full_name='apollo.drivers.racobit_radar.RadarConf.send_ext_info_valid', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort_index_valid', full_name='apollo.drivers.racobit_radar.RadarConf.sort_index_valid', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_in_nvm_valid', full_name='apollo.drivers.racobit_radar.RadarConf.store_in_nvm_valid', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctrl_relay_valid', full_name='apollo.drivers.racobit_radar.RadarConf.ctrl_relay_valid', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rcs_threshold_valid', full_name='apollo.drivers.racobit_radar.RadarConf.rcs_threshold_valid', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_distance', full_name='apollo.drivers.racobit_radar.RadarConf.max_distance', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=248,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='apollo.drivers.racobit_radar.RadarConf.sensor_id', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_type', full_name='apollo.drivers.racobit_radar.RadarConf.output_type', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radar_power', full_name='apollo.drivers.racobit_radar.RadarConf.radar_power', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctrl_relay', full_name='apollo.drivers.racobit_radar.RadarConf.ctrl_relay', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='send_ext_info', full_name='apollo.drivers.racobit_radar.RadarConf.send_ext_info', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='send_quality', full_name='apollo.drivers.racobit_radar.RadarConf.send_quality', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort_index', full_name='apollo.drivers.racobit_radar.RadarConf.sort_index', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_in_nvm', full_name='apollo.drivers.racobit_radar.RadarConf.store_in_nvm', index=18,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rcs_threshold', full_name='apollo.drivers.racobit_radar.RadarConf.rcs_threshold', index=19,
      number=20, type=14, cpp_type=8, label=1,
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
  serialized_start=341,
  serialized_end=1066,
)


_RACOBITRADARCONF = _descriptor.Descriptor(
  name='RacobitRadarConf',
  full_name='apollo.drivers.racobit_radar.RacobitRadarConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='can_conf', full_name='apollo.drivers.racobit_radar.RacobitRadarConf.can_conf', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radar_conf', full_name='apollo.drivers.racobit_radar.RacobitRadarConf.radar_conf', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1069,
  serialized_end=1205,
)

_CANCONF.fields_by_name['can_card_parameter'].message_type = modules_dot_drivers_dot_canbus_dot_proto_dot_can__card__parameter__pb2._CANCARDPARAMETER
_RADARCONF.fields_by_name['output_type'].enum_type = _OUTPUTTYPE
_RADARCONF.fields_by_name['rcs_threshold'].enum_type = _RCSTHRESHOLD
_RACOBITRADARCONF.fields_by_name['can_conf'].message_type = _CANCONF
_RACOBITRADARCONF.fields_by_name['radar_conf'].message_type = _RADARCONF
DESCRIPTOR.message_types_by_name['CanConf'] = _CANCONF
DESCRIPTOR.message_types_by_name['RadarConf'] = _RADARCONF
DESCRIPTOR.message_types_by_name['RacobitRadarConf'] = _RACOBITRADARCONF
DESCRIPTOR.enum_types_by_name['OutputType'] = _OUTPUTTYPE
DESCRIPTOR.enum_types_by_name['RcsThreshold'] = _RCSTHRESHOLD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CanConf = _reflection.GeneratedProtocolMessageType('CanConf', (_message.Message,), dict(
  DESCRIPTOR = _CANCONF,
  __module__ = 'modules.drivers.radar.racobit_radar.proto.racobit_radar_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.racobit_radar.CanConf)
  ))
_sym_db.RegisterMessage(CanConf)

RadarConf = _reflection.GeneratedProtocolMessageType('RadarConf', (_message.Message,), dict(
  DESCRIPTOR = _RADARCONF,
  __module__ = 'modules.drivers.radar.racobit_radar.proto.racobit_radar_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.racobit_radar.RadarConf)
  ))
_sym_db.RegisterMessage(RadarConf)

RacobitRadarConf = _reflection.GeneratedProtocolMessageType('RacobitRadarConf', (_message.Message,), dict(
  DESCRIPTOR = _RACOBITRADARCONF,
  __module__ = 'modules.drivers.radar.racobit_radar.proto.racobit_radar_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.racobit_radar.RacobitRadarConf)
  ))
_sym_db.RegisterMessage(RacobitRadarConf)


# @@protoc_insertion_point(module_scope)
