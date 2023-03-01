# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/control/proto/lat_controller_conf.proto

import sys

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.control.proto import \
    gain_scheduler_conf_pb2 as \
    modules_dot_control_dot_proto_dot_gain__scheduler__conf__pb2
from modules.control.proto import \
    leadlag_conf_pb2 as modules_dot_control_dot_proto_dot_leadlag__conf__pb2
from modules.control.proto import \
    mrac_conf_pb2 as modules_dot_control_dot_proto_dot_mrac__conf__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/control/proto/lat_controller_conf.proto',
  package='apollo.control',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n/modules/control/proto/lat_controller_conf.proto\x12\x0e\x61pollo.control\x1a/modules/control/proto/gain_scheduler_conf.proto\x1a(modules/control/proto/leadlag_conf.proto\x1a%modules/control/proto/mrac_conf.proto\"\xc4\x06\n\x11LatControllerConf\x12\n\n\x02ts\x18\x01 \x01(\x01\x12\x16\n\x0epreview_window\x18\x02 \x01(\x05\x12\n\n\x02\x63\x66\x18\x03 \x01(\x01\x12\n\n\x02\x63r\x18\x04 \x01(\x01\x12\x0f\n\x07mass_fl\x18\x05 \x01(\x05\x12\x0f\n\x07mass_fr\x18\x06 \x01(\x05\x12\x0f\n\x07mass_rl\x18\x07 \x01(\x05\x12\x0f\n\x07mass_rr\x18\x08 \x01(\x05\x12\x0b\n\x03\x65ps\x18\t \x01(\x01\x12\x10\n\x08matrix_q\x18\n \x03(\x01\x12\x18\n\x10reverse_matrix_q\x18\x0b \x03(\x01\x12\x13\n\x0b\x63utoff_freq\x18\x0c \x01(\x05\x12\x1f\n\x17mean_filter_window_size\x18\r \x01(\x05\x12\x15\n\rmax_iteration\x18\x0e \x01(\x05\x12 \n\x18max_lateral_acceleration\x18\x0f \x01(\x01\x12=\n\x16lat_err_gain_scheduler\x18\x10 \x01(\x0b\x32\x1d.apollo.control.GainScheduler\x12\x41\n\x1aheading_err_gain_scheduler\x18\x11 \x01(\x0b\x32\x1d.apollo.control.GainScheduler\x12\x39\n\x14reverse_leadlag_conf\x18\x12 \x01(\x0b\x32\x1b.apollo.control.LeadlagConf\x12\x32\n#enable_reverse_leadlag_compensation\x18\x13 \x01(\x08:\x05\x66\x61lse\x12-\n\x1e\x65nable_look_ahead_back_control\x18\x14 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\x11lookahead_station\x18\x15 \x01(\x01:\x01\x30\x12\x1b\n\x10lookback_station\x18\x16 \x01(\x01:\x01\x30\x12\x31\n\x0fsteer_mrac_conf\x18\x17 \x01(\x0b\x32\x18.apollo.control.MracConf\x12(\n\x19\x65nable_steer_mrac_control\x18\x18 \x01(\x08:\x05\x66\x61lse\x12\'\n\x1clookahead_station_high_speed\x18\x19 \x01(\x01:\x01\x30\x12&\n\x1blookback_station_high_speed\x18\x1a \x01(\x01:\x01\x30')
  ,
  dependencies=[modules_dot_control_dot_proto_dot_gain__scheduler__conf__pb2.DESCRIPTOR,modules_dot_control_dot_proto_dot_leadlag__conf__pb2.DESCRIPTOR,modules_dot_control_dot_proto_dot_mrac__conf__pb2.DESCRIPTOR,])




_LATCONTROLLERCONF = _descriptor.Descriptor(
  name='LatControllerConf',
  full_name='apollo.control.LatControllerConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ts', full_name='apollo.control.LatControllerConf.ts', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preview_window', full_name='apollo.control.LatControllerConf.preview_window', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cf', full_name='apollo.control.LatControllerConf.cf', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cr', full_name='apollo.control.LatControllerConf.cr', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mass_fl', full_name='apollo.control.LatControllerConf.mass_fl', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mass_fr', full_name='apollo.control.LatControllerConf.mass_fr', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mass_rl', full_name='apollo.control.LatControllerConf.mass_rl', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mass_rr', full_name='apollo.control.LatControllerConf.mass_rr', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eps', full_name='apollo.control.LatControllerConf.eps', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='matrix_q', full_name='apollo.control.LatControllerConf.matrix_q', index=9,
      number=10, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reverse_matrix_q', full_name='apollo.control.LatControllerConf.reverse_matrix_q', index=10,
      number=11, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cutoff_freq', full_name='apollo.control.LatControllerConf.cutoff_freq', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean_filter_window_size', full_name='apollo.control.LatControllerConf.mean_filter_window_size', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_iteration', full_name='apollo.control.LatControllerConf.max_iteration', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_lateral_acceleration', full_name='apollo.control.LatControllerConf.max_lateral_acceleration', index=14,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lat_err_gain_scheduler', full_name='apollo.control.LatControllerConf.lat_err_gain_scheduler', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading_err_gain_scheduler', full_name='apollo.control.LatControllerConf.heading_err_gain_scheduler', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reverse_leadlag_conf', full_name='apollo.control.LatControllerConf.reverse_leadlag_conf', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_reverse_leadlag_compensation', full_name='apollo.control.LatControllerConf.enable_reverse_leadlag_compensation', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_look_ahead_back_control', full_name='apollo.control.LatControllerConf.enable_look_ahead_back_control', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lookahead_station', full_name='apollo.control.LatControllerConf.lookahead_station', index=20,
      number=21, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lookback_station', full_name='apollo.control.LatControllerConf.lookback_station', index=21,
      number=22, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steer_mrac_conf', full_name='apollo.control.LatControllerConf.steer_mrac_conf', index=22,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_steer_mrac_control', full_name='apollo.control.LatControllerConf.enable_steer_mrac_control', index=23,
      number=24, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lookahead_station_high_speed', full_name='apollo.control.LatControllerConf.lookahead_station_high_speed', index=24,
      number=25, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lookback_station_high_speed', full_name='apollo.control.LatControllerConf.lookback_station_high_speed', index=25,
      number=26, type=1, cpp_type=5, label=1,
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
  serialized_start=198,
  serialized_end=1034,
)

_LATCONTROLLERCONF.fields_by_name['lat_err_gain_scheduler'].message_type = modules_dot_control_dot_proto_dot_gain__scheduler__conf__pb2._GAINSCHEDULER
_LATCONTROLLERCONF.fields_by_name['heading_err_gain_scheduler'].message_type = modules_dot_control_dot_proto_dot_gain__scheduler__conf__pb2._GAINSCHEDULER
_LATCONTROLLERCONF.fields_by_name['reverse_leadlag_conf'].message_type = modules_dot_control_dot_proto_dot_leadlag__conf__pb2._LEADLAGCONF
_LATCONTROLLERCONF.fields_by_name['steer_mrac_conf'].message_type = modules_dot_control_dot_proto_dot_mrac__conf__pb2._MRACCONF
DESCRIPTOR.message_types_by_name['LatControllerConf'] = _LATCONTROLLERCONF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LatControllerConf = _reflection.GeneratedProtocolMessageType('LatControllerConf', (_message.Message,), dict(
  DESCRIPTOR = _LATCONTROLLERCONF,
  __module__ = 'modules.control.proto.lat_controller_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.control.LatControllerConf)
  ))
_sym_db.RegisterMessage(LatControllerConf)


# @@protoc_insertion_point(module_scope)
