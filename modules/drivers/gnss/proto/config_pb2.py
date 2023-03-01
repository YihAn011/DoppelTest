# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/gnss/proto/config.proto

import sys

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/drivers/gnss/proto/config.proto',
  package='apollo.drivers.gnss.config',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\'modules/drivers/gnss/proto/config.proto\x12\x1a\x61pollo.drivers.gnss.config\"\xd1\x05\n\x06Stream\x12\x39\n\x06\x66ormat\x18\x01 \x01(\x0e\x32).apollo.drivers.gnss.config.Stream.Format\x12;\n\x06serial\x18\x02 \x01(\x0b\x32).apollo.drivers.gnss.config.Stream.SerialH\x00\x12\x35\n\x03tcp\x18\x03 \x01(\x0b\x32&.apollo.drivers.gnss.config.Stream.TcpH\x00\x12\x35\n\x03udp\x18\x04 \x01(\x0b\x32&.apollo.drivers.gnss.config.Stream.UdpH\x00\x12\x39\n\x05ntrip\x18\x05 \x01(\x0b\x32(.apollo.drivers.gnss.config.Stream.NtripH\x00\x12\x15\n\rpush_location\x18\x06 \x01(\x08\x1a\x31\n\x06Serial\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\x0c\x12\x17\n\tbaud_rate\x18\x02 \x01(\x05:\x04\x39\x36\x30\x30\x1a*\n\x03Tcp\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x12\n\x04port\x18\x02 \x01(\x05:\x04\x33\x30\x30\x31\x1a*\n\x03Udp\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x12\n\x04port\x18\x02 \x01(\x05:\x04\x33\x30\x30\x31\x1ax\n\x05Ntrip\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x12\n\x04port\x18\x02 \x01(\x05:\x04\x32\x31\x30\x31\x12\x13\n\x0bmount_point\x18\x03 \x01(\x0c\x12\x0c\n\x04user\x18\x04 \x01(\x0c\x12\x10\n\x08password\x18\x05 \x01(\x0c\x12\x15\n\ttimeout_s\x18\x06 \x01(\r:\x02\x33\x30\"\x81\x01\n\x06\x46ormat\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04NMEA\x10\x01\x12\x0b\n\x07RTCM_V2\x10\x02\x12\x0b\n\x07RTCM_V3\x10\x03\x12\x10\n\x0cNOVATEL_TEXT\x10\n\x12\x12\n\x0eNOVATEL_BINARY\x10\x0b\x12\x0e\n\nUBLOX_TEXT\x10\x14\x12\x10\n\x0cUBLOX_BINARY\x10\x15\x42\x06\n\x04type\"+\n\rNovatelConfig\x12\x1a\n\x0fimu_orientation\x18\x01 \x01(\x05:\x01\x35\"\r\n\x0bUbloxConfig\"U\n\x02TF\x12\x17\n\x08\x66rame_id\x18\x01 \x01(\t:\x05world\x12\x1f\n\x0e\x63hild_frame_id\x18\x02 \x01(\t:\x07novatel\x12\x15\n\x06\x65nable\x18\x03 \x01(\x08:\x05\x66\x61lse\"\xe1\x05\n\x06\x43onfig\x12\x30\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\".apollo.drivers.gnss.config.Stream\x12\x33\n\x07\x63ommand\x18\x02 \x01(\x0b\x32\".apollo.drivers.gnss.config.Stream\x12\x34\n\x08rtk_from\x18\x03 \x01(\x0b\x32\".apollo.drivers.gnss.config.Stream\x12\x32\n\x06rtk_to\x18\x04 \x01(\x0b\x32\".apollo.drivers.gnss.config.Stream\x12\x16\n\x0elogin_commands\x18\x05 \x03(\x0c\x12\x17\n\x0flogout_commands\x18\x06 \x03(\x0c\x12\x43\n\x0enovatel_config\x18\x07 \x01(\x0b\x32).apollo.drivers.gnss.config.NovatelConfigH\x00\x12?\n\x0cublox_config\x18\x08 \x01(\x0b\x32\'.apollo.drivers.gnss.config.UbloxConfigH\x00\x12M\n\x11rtk_solution_type\x18\t \x01(\x0e\x32\x32.apollo.drivers.gnss.config.Config.RtkSolutionType\x12\x35\n\x08imu_type\x18\n \x01(\x0e\x32#.apollo.drivers.gnss.config.ImuType\x12\x12\n\nproj4_text\x18\x0b \x01(\t\x12*\n\x02tf\x18\x0c \x01(\x0b\x32\x1e.apollo.drivers.gnss.config.TF\x12\x18\n\x10wheel_parameters\x18\r \x01(\t\x12\x15\n\rgpsbin_folder\x18\x0e \x01(\t\"G\n\x0fRtkSolutionType\x12\x19\n\x15RTK_RECEIVER_SOLUTION\x10\x01\x12\x19\n\x15RTK_SOFTWARE_SOLUTION\x10\x02\x42\x0f\n\rdevice_config*\xa6\x01\n\x07ImuType\x12\r\n\tIMAR_FSAS\x10\r\x12\x0b\n\x07ISA100C\x10\x1a\x12\r\n\tADIS16488\x10\x1f\x12\x0b\n\x07STIM300\x10 \x12\n\n\x06ISA100\x10\"\x12\x10\n\x0cISA100_400HZ\x10&\x12\x11\n\rISA100C_400HZ\x10\'\x12\x0e\n\nCPT_XW5651\x10(\x12\t\n\x05G320N\x10)\x12\t\n\x05UM442\x10*\x12\x0c\n\x08IAM20680\x10\x39')
)

_IMUTYPE = _descriptor.EnumDescriptor(
  name='ImuType',
  full_name='apollo.drivers.gnss.config.ImuType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IMAR_FSAS', index=0, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISA100C', index=1, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADIS16488', index=2, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STIM300', index=3, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISA100', index=4, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISA100_400HZ', index=5, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISA100C_400HZ', index=6, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CPT_XW5651', index=7, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='G320N', index=8, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UM442', index=9, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAM20680', index=10, number=57,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1683,
  serialized_end=1849,
)
_sym_db.RegisterEnumDescriptor(_IMUTYPE)

ImuType = enum_type_wrapper.EnumTypeWrapper(_IMUTYPE)
IMAR_FSAS = 13
ISA100C = 26
ADIS16488 = 31
STIM300 = 32
ISA100 = 34
ISA100_400HZ = 38
ISA100C_400HZ = 39
CPT_XW5651 = 40
G320N = 41
UM442 = 42
IAM20680 = 57


_STREAM_FORMAT = _descriptor.EnumDescriptor(
  name='Format',
  full_name='apollo.drivers.gnss.config.Stream.Format',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NMEA', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTCM_V2', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTCM_V3', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOVATEL_TEXT', index=4, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOVATEL_BINARY', index=5, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UBLOX_TEXT', index=6, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UBLOX_BINARY', index=7, number=21,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=656,
  serialized_end=785,
)
_sym_db.RegisterEnumDescriptor(_STREAM_FORMAT)

_CONFIG_RTKSOLUTIONTYPE = _descriptor.EnumDescriptor(
  name='RtkSolutionType',
  full_name='apollo.drivers.gnss.config.Config.RtkSolutionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RTK_RECEIVER_SOLUTION', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTK_SOFTWARE_SOLUTION', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1592,
  serialized_end=1663,
)
_sym_db.RegisterEnumDescriptor(_CONFIG_RTKSOLUTIONTYPE)


_STREAM_SERIAL = _descriptor.Descriptor(
  name='Serial',
  full_name='apollo.drivers.gnss.config.Stream.Serial',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='apollo.drivers.gnss.config.Stream.Serial.device', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='baud_rate', full_name='apollo.drivers.gnss.config.Stream.Serial.baud_rate', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=9600,
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
  serialized_start=394,
  serialized_end=443,
)

_STREAM_TCP = _descriptor.Descriptor(
  name='Tcp',
  full_name='apollo.drivers.gnss.config.Stream.Tcp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='apollo.drivers.gnss.config.Stream.Tcp.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='apollo.drivers.gnss.config.Stream.Tcp.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3001,
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
  serialized_start=445,
  serialized_end=487,
)

_STREAM_UDP = _descriptor.Descriptor(
  name='Udp',
  full_name='apollo.drivers.gnss.config.Stream.Udp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='apollo.drivers.gnss.config.Stream.Udp.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='apollo.drivers.gnss.config.Stream.Udp.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3001,
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
  serialized_start=489,
  serialized_end=531,
)

_STREAM_NTRIP = _descriptor.Descriptor(
  name='Ntrip',
  full_name='apollo.drivers.gnss.config.Stream.Ntrip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='apollo.drivers.gnss.config.Stream.Ntrip.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='apollo.drivers.gnss.config.Stream.Ntrip.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2101,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mount_point', full_name='apollo.drivers.gnss.config.Stream.Ntrip.mount_point', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='apollo.drivers.gnss.config.Stream.Ntrip.user', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='apollo.drivers.gnss.config.Stream.Ntrip.password', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout_s', full_name='apollo.drivers.gnss.config.Stream.Ntrip.timeout_s', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=30,
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
  serialized_start=533,
  serialized_end=653,
)

_STREAM = _descriptor.Descriptor(
  name='Stream',
  full_name='apollo.drivers.gnss.config.Stream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='format', full_name='apollo.drivers.gnss.config.Stream.format', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serial', full_name='apollo.drivers.gnss.config.Stream.serial', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tcp', full_name='apollo.drivers.gnss.config.Stream.tcp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='udp', full_name='apollo.drivers.gnss.config.Stream.udp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ntrip', full_name='apollo.drivers.gnss.config.Stream.ntrip', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='push_location', full_name='apollo.drivers.gnss.config.Stream.push_location', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STREAM_SERIAL, _STREAM_TCP, _STREAM_UDP, _STREAM_NTRIP, ],
  enum_types=[
    _STREAM_FORMAT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='apollo.drivers.gnss.config.Stream.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=72,
  serialized_end=793,
)


_NOVATELCONFIG = _descriptor.Descriptor(
  name='NovatelConfig',
  full_name='apollo.drivers.gnss.config.NovatelConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='imu_orientation', full_name='apollo.drivers.gnss.config.NovatelConfig.imu_orientation', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=5,
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
  serialized_start=795,
  serialized_end=838,
)


_UBLOXCONFIG = _descriptor.Descriptor(
  name='UbloxConfig',
  full_name='apollo.drivers.gnss.config.UbloxConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=840,
  serialized_end=853,
)


_TF = _descriptor.Descriptor(
  name='TF',
  full_name='apollo.drivers.gnss.config.TF',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_id', full_name='apollo.drivers.gnss.config.TF.frame_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("world").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='child_frame_id', full_name='apollo.drivers.gnss.config.TF.child_frame_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("novatel").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable', full_name='apollo.drivers.gnss.config.TF.enable', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=855,
  serialized_end=940,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='apollo.drivers.gnss.config.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='apollo.drivers.gnss.config.Config.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='apollo.drivers.gnss.config.Config.command', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rtk_from', full_name='apollo.drivers.gnss.config.Config.rtk_from', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rtk_to', full_name='apollo.drivers.gnss.config.Config.rtk_to', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='login_commands', full_name='apollo.drivers.gnss.config.Config.login_commands', index=4,
      number=5, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logout_commands', full_name='apollo.drivers.gnss.config.Config.logout_commands', index=5,
      number=6, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='novatel_config', full_name='apollo.drivers.gnss.config.Config.novatel_config', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ublox_config', full_name='apollo.drivers.gnss.config.Config.ublox_config', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rtk_solution_type', full_name='apollo.drivers.gnss.config.Config.rtk_solution_type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imu_type', full_name='apollo.drivers.gnss.config.Config.imu_type', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=13,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proj4_text', full_name='apollo.drivers.gnss.config.Config.proj4_text', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tf', full_name='apollo.drivers.gnss.config.Config.tf', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wheel_parameters', full_name='apollo.drivers.gnss.config.Config.wheel_parameters', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpsbin_folder', full_name='apollo.drivers.gnss.config.Config.gpsbin_folder', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONFIG_RTKSOLUTIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='device_config', full_name='apollo.drivers.gnss.config.Config.device_config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=943,
  serialized_end=1680,
)

_STREAM_SERIAL.containing_type = _STREAM
_STREAM_TCP.containing_type = _STREAM
_STREAM_UDP.containing_type = _STREAM
_STREAM_NTRIP.containing_type = _STREAM
_STREAM.fields_by_name['format'].enum_type = _STREAM_FORMAT
_STREAM.fields_by_name['serial'].message_type = _STREAM_SERIAL
_STREAM.fields_by_name['tcp'].message_type = _STREAM_TCP
_STREAM.fields_by_name['udp'].message_type = _STREAM_UDP
_STREAM.fields_by_name['ntrip'].message_type = _STREAM_NTRIP
_STREAM_FORMAT.containing_type = _STREAM
_STREAM.oneofs_by_name['type'].fields.append(
  _STREAM.fields_by_name['serial'])
_STREAM.fields_by_name['serial'].containing_oneof = _STREAM.oneofs_by_name['type']
_STREAM.oneofs_by_name['type'].fields.append(
  _STREAM.fields_by_name['tcp'])
_STREAM.fields_by_name['tcp'].containing_oneof = _STREAM.oneofs_by_name['type']
_STREAM.oneofs_by_name['type'].fields.append(
  _STREAM.fields_by_name['udp'])
_STREAM.fields_by_name['udp'].containing_oneof = _STREAM.oneofs_by_name['type']
_STREAM.oneofs_by_name['type'].fields.append(
  _STREAM.fields_by_name['ntrip'])
_STREAM.fields_by_name['ntrip'].containing_oneof = _STREAM.oneofs_by_name['type']
_CONFIG.fields_by_name['data'].message_type = _STREAM
_CONFIG.fields_by_name['command'].message_type = _STREAM
_CONFIG.fields_by_name['rtk_from'].message_type = _STREAM
_CONFIG.fields_by_name['rtk_to'].message_type = _STREAM
_CONFIG.fields_by_name['novatel_config'].message_type = _NOVATELCONFIG
_CONFIG.fields_by_name['ublox_config'].message_type = _UBLOXCONFIG
_CONFIG.fields_by_name['rtk_solution_type'].enum_type = _CONFIG_RTKSOLUTIONTYPE
_CONFIG.fields_by_name['imu_type'].enum_type = _IMUTYPE
_CONFIG.fields_by_name['tf'].message_type = _TF
_CONFIG_RTKSOLUTIONTYPE.containing_type = _CONFIG
_CONFIG.oneofs_by_name['device_config'].fields.append(
  _CONFIG.fields_by_name['novatel_config'])
_CONFIG.fields_by_name['novatel_config'].containing_oneof = _CONFIG.oneofs_by_name['device_config']
_CONFIG.oneofs_by_name['device_config'].fields.append(
  _CONFIG.fields_by_name['ublox_config'])
_CONFIG.fields_by_name['ublox_config'].containing_oneof = _CONFIG.oneofs_by_name['device_config']
DESCRIPTOR.message_types_by_name['Stream'] = _STREAM
DESCRIPTOR.message_types_by_name['NovatelConfig'] = _NOVATELCONFIG
DESCRIPTOR.message_types_by_name['UbloxConfig'] = _UBLOXCONFIG
DESCRIPTOR.message_types_by_name['TF'] = _TF
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.enum_types_by_name['ImuType'] = _IMUTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Stream = _reflection.GeneratedProtocolMessageType('Stream', (_message.Message,), dict(

  Serial = _reflection.GeneratedProtocolMessageType('Serial', (_message.Message,), dict(
    DESCRIPTOR = _STREAM_SERIAL,
    __module__ = 'modules.drivers.gnss.proto.config_pb2'
    # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.config.Stream.Serial)
    ))
  ,

  Tcp = _reflection.GeneratedProtocolMessageType('Tcp', (_message.Message,), dict(
    DESCRIPTOR = _STREAM_TCP,
    __module__ = 'modules.drivers.gnss.proto.config_pb2'
    # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.config.Stream.Tcp)
    ))
  ,

  Udp = _reflection.GeneratedProtocolMessageType('Udp', (_message.Message,), dict(
    DESCRIPTOR = _STREAM_UDP,
    __module__ = 'modules.drivers.gnss.proto.config_pb2'
    # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.config.Stream.Udp)
    ))
  ,

  Ntrip = _reflection.GeneratedProtocolMessageType('Ntrip', (_message.Message,), dict(
    DESCRIPTOR = _STREAM_NTRIP,
    __module__ = 'modules.drivers.gnss.proto.config_pb2'
    # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.config.Stream.Ntrip)
    ))
  ,
  DESCRIPTOR = _STREAM,
  __module__ = 'modules.drivers.gnss.proto.config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.config.Stream)
  ))
_sym_db.RegisterMessage(Stream)
_sym_db.RegisterMessage(Stream.Serial)
_sym_db.RegisterMessage(Stream.Tcp)
_sym_db.RegisterMessage(Stream.Udp)
_sym_db.RegisterMessage(Stream.Ntrip)

NovatelConfig = _reflection.GeneratedProtocolMessageType('NovatelConfig', (_message.Message,), dict(
  DESCRIPTOR = _NOVATELCONFIG,
  __module__ = 'modules.drivers.gnss.proto.config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.config.NovatelConfig)
  ))
_sym_db.RegisterMessage(NovatelConfig)

UbloxConfig = _reflection.GeneratedProtocolMessageType('UbloxConfig', (_message.Message,), dict(
  DESCRIPTOR = _UBLOXCONFIG,
  __module__ = 'modules.drivers.gnss.proto.config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.config.UbloxConfig)
  ))
_sym_db.RegisterMessage(UbloxConfig)

TF = _reflection.GeneratedProtocolMessageType('TF', (_message.Message,), dict(
  DESCRIPTOR = _TF,
  __module__ = 'modules.drivers.gnss.proto.config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.config.TF)
  ))
_sym_db.RegisterMessage(TF)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'modules.drivers.gnss.proto.config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.config.Config)
  ))
_sym_db.RegisterMessage(Config)


# @@protoc_insertion_point(module_scope)
