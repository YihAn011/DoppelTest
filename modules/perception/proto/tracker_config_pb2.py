# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/proto/tracker_config.proto

import sys

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/perception/proto/tracker_config.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n-modules/perception/proto/tracker_config.proto\"R\n\rMatcherConfig\x12\x1f\n\x12max_match_distance\x18\x01 \x01(\x01:\x03\x32.5\x12 \n\x14\x62ound_match_distance\x18\x02 \x01(\x01:\x02\x31\x30')
)




_MATCHERCONFIG = _descriptor.Descriptor(
  name='MatcherConfig',
  full_name='MatcherConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_match_distance', full_name='MatcherConfig.max_match_distance', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(2.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bound_match_distance', full_name='MatcherConfig.bound_match_distance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(10),
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
  serialized_start=49,
  serialized_end=131,
)

DESCRIPTOR.message_types_by_name['MatcherConfig'] = _MATCHERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MatcherConfig = _reflection.GeneratedProtocolMessageType('MatcherConfig', (_message.Message,), dict(
  DESCRIPTOR = _MATCHERCONFIG,
  __module__ = 'modules.perception.proto.tracker_config_pb2'
  # @@protoc_insertion_point(class_scope:MatcherConfig)
  ))
_sym_db.RegisterMessage(MatcherConfig)


# @@protoc_insertion_point(module_scope)
