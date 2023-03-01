# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common/proto/drive_state.proto

import sys

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/common/proto/drive_state.proto',
  package='apollo.common',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n&modules/common/proto/drive_state.proto\x12\rapollo.common\"\xcd\x01\n\x0c\x45ngageAdvice\x12\x43\n\x06\x61\x64vice\x18\x01 \x01(\x0e\x32\".apollo.common.EngageAdvice.Advice:\x0f\x44ISALLOW_ENGAGE\x12\x0e\n\x06reason\x18\x02 \x01(\t\"h\n\x06\x41\x64vice\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0f\x44ISALLOW_ENGAGE\x10\x01\x12\x13\n\x0fREADY_TO_ENGAGE\x10\x02\x12\x10\n\x0cKEEP_ENGAGED\x10\x03\x12\x15\n\x11PREPARE_DISENGAGE\x10\x04')
)



_ENGAGEADVICE_ADVICE = _descriptor.EnumDescriptor(
  name='Advice',
  full_name='apollo.common.EngageAdvice.Advice',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISALLOW_ENGAGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY_TO_ENGAGE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEEP_ENGAGED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREPARE_DISENGAGE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=159,
  serialized_end=263,
)
_sym_db.RegisterEnumDescriptor(_ENGAGEADVICE_ADVICE)


_ENGAGEADVICE = _descriptor.Descriptor(
  name='EngageAdvice',
  full_name='apollo.common.EngageAdvice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='advice', full_name='apollo.common.EngageAdvice.advice', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='apollo.common.EngageAdvice.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENGAGEADVICE_ADVICE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=263,
)

_ENGAGEADVICE.fields_by_name['advice'].enum_type = _ENGAGEADVICE_ADVICE
_ENGAGEADVICE_ADVICE.containing_type = _ENGAGEADVICE
DESCRIPTOR.message_types_by_name['EngageAdvice'] = _ENGAGEADVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EngageAdvice = _reflection.GeneratedProtocolMessageType('EngageAdvice', (_message.Message,), dict(
  DESCRIPTOR = _ENGAGEADVICE,
  __module__ = 'modules.common.proto.drive_state_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.EngageAdvice)
  ))
_sym_db.RegisterMessage(EngageAdvice)


# @@protoc_insertion_point(module_scope)
