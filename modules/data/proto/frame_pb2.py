# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/data/proto/frame.proto

import sys

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/data/proto/frame.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1emodules/data/proto/frame.proto\"*\n\x07Vector3\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"O\n\x07Vector4\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\t\n\x01i\x18\x04 \x01(\x01\x12\x18\n\tis_ground\x18\x05 \x01(\x08:\x05\x66\x61lse\"8\n\nQuaternion\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\t\n\x01w\x18\x04 \x01(\x01\"\x85\x01\n\x07GPSPose\x12\x0b\n\x03lat\x18\x01 \x01(\x01\x12\x0b\n\x03lon\x18\x02 \x01(\x01\x12\x0f\n\x07\x62\x65\x61ring\x18\x03 \x01(\x01\x12\t\n\x01x\x18\x04 \x01(\x01\x12\t\n\x01y\x18\x05 \x01(\x01\x12\t\n\x01z\x18\x06 \x01(\x01\x12\n\n\x02qw\x18\x07 \x01(\x01\x12\n\n\x02qx\x18\x08 \x01(\x01\x12\n\n\x02qy\x18\t \x01(\x01\x12\n\n\x02qz\x18\n \x01(\x01\"\xf8\x01\n\x0b\x43\x61meraImage\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\x11\n\timage_url\x18\x02 \x01(\t\x12\x1a\n\x08position\x18\x03 \x01(\x0b\x32\x08.Vector3\x12\x1c\n\x07heading\x18\x04 \x01(\x0b\x32\x0b.Quaternion\x12\n\n\x02\x66x\x18\x05 \x01(\x01\x12\n\n\x02\x66y\x18\x06 \x01(\x01\x12\n\n\x02\x63x\x18\x07 \x01(\x01\x12\n\n\x02\x63y\x18\x08 \x01(\x01\x12\x0c\n\x04skew\x18\t \x01(\x01\x12\n\n\x02k1\x18\n \x01(\x01\x12\n\n\x02k2\x18\x0b \x01(\x01\x12\n\n\x02k3\x18\x0c \x01(\x01\x12\n\n\x02p1\x18\r \x01(\x01\x12\n\n\x02p2\x18\x0e \x01(\x01\x12\x0f\n\x07\x63hannel\x18\x0f \x01(\t\"\x8c\x01\n\nRadarPoint\x12\x1a\n\x08position\x18\x01 \x01(\x0b\x32\x08.Vector3\x12\x1b\n\tdirection\x18\x02 \x01(\x0b\x32\x08.Vector3\x12#\n\x04type\x18\x03 \x01(\x0e\x32\x15.RadarPoint.RadarType\" \n\tRadarType\x12\t\n\x05\x46RONT\x10\x01\x12\x08\n\x04REAR\x10\x02\"\x86\x02\n\x05\x46rame\x12!\n\x0f\x64\x65vice_position\x18\x01 \x01(\x0b\x32\x08.Vector3\x12#\n\x0e\x64\x65vice_heading\x18\x02 \x01(\x0b\x32\x0b.Quaternion\x12!\n\x0f\x64\x65vice_gps_pose\x18\x03 \x01(\x0b\x32\x08.GPSPose\x12\x18\n\x06points\x18\x04 \x03(\x0b\x32\x08.Vector4\x12!\n\x0cradar_points\x18\x05 \x03(\x0b\x32\x0b.RadarPoint\x12\x1c\n\x06images\x18\x06 \x03(\x0b\x32\x0c.CameraImage\x12\x11\n\ttimestamp\x18\x07 \x01(\x01\x12\x11\n\tframe_seq\x18\x08 \x01(\x05\x12\x11\n\tdata_file\x18\t \x01(\t')
)



_RADARPOINT_RADARTYPE = _descriptor.EnumDescriptor(
  name='RadarType',
  full_name='RadarPoint.RadarType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FRONT', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REAR', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=713,
  serialized_end=745,
)
_sym_db.RegisterEnumDescriptor(_RADARPOINT_RADARTYPE)


_VECTOR3 = _descriptor.Descriptor(
  name='Vector3',
  full_name='Vector3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Vector3.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='Vector3.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='Vector3.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=34,
  serialized_end=76,
)


_VECTOR4 = _descriptor.Descriptor(
  name='Vector4',
  full_name='Vector4',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Vector4.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='Vector4.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='Vector4.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i', full_name='Vector4.i', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_ground', full_name='Vector4.is_ground', index=4,
      number=5, type=8, cpp_type=7, label=1,
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
  serialized_start=78,
  serialized_end=157,
)


_QUATERNION = _descriptor.Descriptor(
  name='Quaternion',
  full_name='Quaternion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Quaternion.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='Quaternion.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='Quaternion.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w', full_name='Quaternion.w', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=159,
  serialized_end=215,
)


_GPSPOSE = _descriptor.Descriptor(
  name='GPSPose',
  full_name='GPSPose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='GPSPose.lat', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon', full_name='GPSPose.lon', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bearing', full_name='GPSPose.bearing', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='GPSPose.x', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='GPSPose.y', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='GPSPose.z', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qw', full_name='GPSPose.qw', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qx', full_name='GPSPose.qx', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qy', full_name='GPSPose.qy', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qz', full_name='GPSPose.qz', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=218,
  serialized_end=351,
)


_CAMERAIMAGE = _descriptor.Descriptor(
  name='CameraImage',
  full_name='CameraImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='CameraImage.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='CameraImage.image_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='CameraImage.position', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading', full_name='CameraImage.heading', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fx', full_name='CameraImage.fx', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fy', full_name='CameraImage.fy', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cx', full_name='CameraImage.cx', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cy', full_name='CameraImage.cy', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skew', full_name='CameraImage.skew', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k1', full_name='CameraImage.k1', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k2', full_name='CameraImage.k2', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k3', full_name='CameraImage.k3', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p1', full_name='CameraImage.p1', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p2', full_name='CameraImage.p2', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='CameraImage.channel', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=354,
  serialized_end=602,
)


_RADARPOINT = _descriptor.Descriptor(
  name='RadarPoint',
  full_name='RadarPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='RadarPoint.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='RadarPoint.direction', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='RadarPoint.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RADARPOINT_RADARTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=605,
  serialized_end=745,
)


_FRAME = _descriptor.Descriptor(
  name='Frame',
  full_name='Frame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_position', full_name='Frame.device_position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_heading', full_name='Frame.device_heading', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_gps_pose', full_name='Frame.device_gps_pose', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='points', full_name='Frame.points', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radar_points', full_name='Frame.radar_points', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='images', full_name='Frame.images', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Frame.timestamp', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_seq', full_name='Frame.frame_seq', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_file', full_name='Frame.data_file', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=748,
  serialized_end=1010,
)

_CAMERAIMAGE.fields_by_name['position'].message_type = _VECTOR3
_CAMERAIMAGE.fields_by_name['heading'].message_type = _QUATERNION
_RADARPOINT.fields_by_name['position'].message_type = _VECTOR3
_RADARPOINT.fields_by_name['direction'].message_type = _VECTOR3
_RADARPOINT.fields_by_name['type'].enum_type = _RADARPOINT_RADARTYPE
_RADARPOINT_RADARTYPE.containing_type = _RADARPOINT
_FRAME.fields_by_name['device_position'].message_type = _VECTOR3
_FRAME.fields_by_name['device_heading'].message_type = _QUATERNION
_FRAME.fields_by_name['device_gps_pose'].message_type = _GPSPOSE
_FRAME.fields_by_name['points'].message_type = _VECTOR4
_FRAME.fields_by_name['radar_points'].message_type = _RADARPOINT
_FRAME.fields_by_name['images'].message_type = _CAMERAIMAGE
DESCRIPTOR.message_types_by_name['Vector3'] = _VECTOR3
DESCRIPTOR.message_types_by_name['Vector4'] = _VECTOR4
DESCRIPTOR.message_types_by_name['Quaternion'] = _QUATERNION
DESCRIPTOR.message_types_by_name['GPSPose'] = _GPSPOSE
DESCRIPTOR.message_types_by_name['CameraImage'] = _CAMERAIMAGE
DESCRIPTOR.message_types_by_name['RadarPoint'] = _RADARPOINT
DESCRIPTOR.message_types_by_name['Frame'] = _FRAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vector3 = _reflection.GeneratedProtocolMessageType('Vector3', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR3,
  __module__ = 'modules.data.proto.frame_pb2'
  # @@protoc_insertion_point(class_scope:Vector3)
  ))
_sym_db.RegisterMessage(Vector3)

Vector4 = _reflection.GeneratedProtocolMessageType('Vector4', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR4,
  __module__ = 'modules.data.proto.frame_pb2'
  # @@protoc_insertion_point(class_scope:Vector4)
  ))
_sym_db.RegisterMessage(Vector4)

Quaternion = _reflection.GeneratedProtocolMessageType('Quaternion', (_message.Message,), dict(
  DESCRIPTOR = _QUATERNION,
  __module__ = 'modules.data.proto.frame_pb2'
  # @@protoc_insertion_point(class_scope:Quaternion)
  ))
_sym_db.RegisterMessage(Quaternion)

GPSPose = _reflection.GeneratedProtocolMessageType('GPSPose', (_message.Message,), dict(
  DESCRIPTOR = _GPSPOSE,
  __module__ = 'modules.data.proto.frame_pb2'
  # @@protoc_insertion_point(class_scope:GPSPose)
  ))
_sym_db.RegisterMessage(GPSPose)

CameraImage = _reflection.GeneratedProtocolMessageType('CameraImage', (_message.Message,), dict(
  DESCRIPTOR = _CAMERAIMAGE,
  __module__ = 'modules.data.proto.frame_pb2'
  # @@protoc_insertion_point(class_scope:CameraImage)
  ))
_sym_db.RegisterMessage(CameraImage)

RadarPoint = _reflection.GeneratedProtocolMessageType('RadarPoint', (_message.Message,), dict(
  DESCRIPTOR = _RADARPOINT,
  __module__ = 'modules.data.proto.frame_pb2'
  # @@protoc_insertion_point(class_scope:RadarPoint)
  ))
_sym_db.RegisterMessage(RadarPoint)

Frame = _reflection.GeneratedProtocolMessageType('Frame', (_message.Message,), dict(
  DESCRIPTOR = _FRAME,
  __module__ = 'modules.data.proto.frame_pb2'
  # @@protoc_insertion_point(class_scope:Frame)
  ))
_sym_db.RegisterMessage(Frame)


# @@protoc_insertion_point(module_scope)
