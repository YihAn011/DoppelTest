# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/storytelling/proto/story.proto

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
  name='modules/storytelling/proto/story.proto',
  package='apollo.storytelling',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n&modules/storytelling/proto/story.proto\x12\x13\x61pollo.storytelling\x1a!modules/common/proto/header.proto\"5\n\x10\x43loseToCrosswalk\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08\x64istance\x18\x02 \x01(\x01:\x03nan\"5\n\x10\x43loseToClearArea\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08\x64istance\x18\x02 \x01(\x01:\x03nan\"\xa5\x01\n\x0f\x43loseToJunction\x12\n\n\x02id\x18\x01 \x01(\t\x12?\n\x04type\x18\x02 \x01(\x0e\x32\x31.apollo.storytelling.CloseToJunction.JunctionType\x12\x15\n\x08\x64istance\x18\x03 \x01(\x01:\x03nan\".\n\x0cJunctionType\x12\x10\n\x0cPNC_JUNCTION\x10\x01\x12\x0c\n\x08JUNCTION\x10\x02\"2\n\rCloseToSignal\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08\x64istance\x18\x02 \x01(\x01:\x03nan\"4\n\x0f\x43loseToStopSign\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08\x64istance\x18\x02 \x01(\x01:\x03nan\"5\n\x10\x43loseToYieldSign\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08\x64istance\x18\x02 \x01(\x01:\x03nan\"\xbb\x03\n\x07Stories\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x42\n\x13\x63lose_to_clear_area\x18\x02 \x01(\x0b\x32%.apollo.storytelling.CloseToClearArea\x12\x41\n\x12\x63lose_to_crosswalk\x18\x03 \x01(\x0b\x32%.apollo.storytelling.CloseToCrosswalk\x12?\n\x11\x63lose_to_junction\x18\x04 \x01(\x0b\x32$.apollo.storytelling.CloseToJunction\x12;\n\x0f\x63lose_to_signal\x18\x05 \x01(\x0b\x32\".apollo.storytelling.CloseToSignal\x12@\n\x12\x63lose_to_stop_sign\x18\x06 \x01(\x0b\x32$.apollo.storytelling.CloseToStopSign\x12\x42\n\x13\x63lose_to_yield_sign\x18\x07 \x01(\x0b\x32%.apollo.storytelling.CloseToYieldSign')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,])



_CLOSETOJUNCTION_JUNCTIONTYPE = _descriptor.EnumDescriptor(
  name='JunctionType',
  full_name='apollo.storytelling.CloseToJunction.JunctionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PNC_JUNCTION', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JUNCTION', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=328,
  serialized_end=374,
)
_sym_db.RegisterEnumDescriptor(_CLOSETOJUNCTION_JUNCTIONTYPE)


_CLOSETOCROSSWALK = _descriptor.Descriptor(
  name='CloseToCrosswalk',
  full_name='apollo.storytelling.CloseToCrosswalk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.storytelling.CloseToCrosswalk.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='apollo.storytelling.CloseToCrosswalk.distance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
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
  serialized_start=98,
  serialized_end=151,
)


_CLOSETOCLEARAREA = _descriptor.Descriptor(
  name='CloseToClearArea',
  full_name='apollo.storytelling.CloseToClearArea',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.storytelling.CloseToClearArea.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='apollo.storytelling.CloseToClearArea.distance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
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
  serialized_start=153,
  serialized_end=206,
)


_CLOSETOJUNCTION = _descriptor.Descriptor(
  name='CloseToJunction',
  full_name='apollo.storytelling.CloseToJunction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.storytelling.CloseToJunction.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='apollo.storytelling.CloseToJunction.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='apollo.storytelling.CloseToJunction.distance', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLOSETOJUNCTION_JUNCTIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=374,
)


_CLOSETOSIGNAL = _descriptor.Descriptor(
  name='CloseToSignal',
  full_name='apollo.storytelling.CloseToSignal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.storytelling.CloseToSignal.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='apollo.storytelling.CloseToSignal.distance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
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
  serialized_start=376,
  serialized_end=426,
)


_CLOSETOSTOPSIGN = _descriptor.Descriptor(
  name='CloseToStopSign',
  full_name='apollo.storytelling.CloseToStopSign',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.storytelling.CloseToStopSign.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='apollo.storytelling.CloseToStopSign.distance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
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
  serialized_start=428,
  serialized_end=480,
)


_CLOSETOYIELDSIGN = _descriptor.Descriptor(
  name='CloseToYieldSign',
  full_name='apollo.storytelling.CloseToYieldSign',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.storytelling.CloseToYieldSign.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='apollo.storytelling.CloseToYieldSign.distance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
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
  serialized_start=482,
  serialized_end=535,
)


_STORIES = _descriptor.Descriptor(
  name='Stories',
  full_name='apollo.storytelling.Stories',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.storytelling.Stories.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_to_clear_area', full_name='apollo.storytelling.Stories.close_to_clear_area', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_to_crosswalk', full_name='apollo.storytelling.Stories.close_to_crosswalk', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_to_junction', full_name='apollo.storytelling.Stories.close_to_junction', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_to_signal', full_name='apollo.storytelling.Stories.close_to_signal', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_to_stop_sign', full_name='apollo.storytelling.Stories.close_to_stop_sign', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_to_yield_sign', full_name='apollo.storytelling.Stories.close_to_yield_sign', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=538,
  serialized_end=981,
)

_CLOSETOJUNCTION.fields_by_name['type'].enum_type = _CLOSETOJUNCTION_JUNCTIONTYPE
_CLOSETOJUNCTION_JUNCTIONTYPE.containing_type = _CLOSETOJUNCTION
_STORIES.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_STORIES.fields_by_name['close_to_clear_area'].message_type = _CLOSETOCLEARAREA
_STORIES.fields_by_name['close_to_crosswalk'].message_type = _CLOSETOCROSSWALK
_STORIES.fields_by_name['close_to_junction'].message_type = _CLOSETOJUNCTION
_STORIES.fields_by_name['close_to_signal'].message_type = _CLOSETOSIGNAL
_STORIES.fields_by_name['close_to_stop_sign'].message_type = _CLOSETOSTOPSIGN
_STORIES.fields_by_name['close_to_yield_sign'].message_type = _CLOSETOYIELDSIGN
DESCRIPTOR.message_types_by_name['CloseToCrosswalk'] = _CLOSETOCROSSWALK
DESCRIPTOR.message_types_by_name['CloseToClearArea'] = _CLOSETOCLEARAREA
DESCRIPTOR.message_types_by_name['CloseToJunction'] = _CLOSETOJUNCTION
DESCRIPTOR.message_types_by_name['CloseToSignal'] = _CLOSETOSIGNAL
DESCRIPTOR.message_types_by_name['CloseToStopSign'] = _CLOSETOSTOPSIGN
DESCRIPTOR.message_types_by_name['CloseToYieldSign'] = _CLOSETOYIELDSIGN
DESCRIPTOR.message_types_by_name['Stories'] = _STORIES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CloseToCrosswalk = _reflection.GeneratedProtocolMessageType('CloseToCrosswalk', (_message.Message,), dict(
  DESCRIPTOR = _CLOSETOCROSSWALK,
  __module__ = 'modules.storytelling.proto.story_pb2'
  # @@protoc_insertion_point(class_scope:apollo.storytelling.CloseToCrosswalk)
  ))
_sym_db.RegisterMessage(CloseToCrosswalk)

CloseToClearArea = _reflection.GeneratedProtocolMessageType('CloseToClearArea', (_message.Message,), dict(
  DESCRIPTOR = _CLOSETOCLEARAREA,
  __module__ = 'modules.storytelling.proto.story_pb2'
  # @@protoc_insertion_point(class_scope:apollo.storytelling.CloseToClearArea)
  ))
_sym_db.RegisterMessage(CloseToClearArea)

CloseToJunction = _reflection.GeneratedProtocolMessageType('CloseToJunction', (_message.Message,), dict(
  DESCRIPTOR = _CLOSETOJUNCTION,
  __module__ = 'modules.storytelling.proto.story_pb2'
  # @@protoc_insertion_point(class_scope:apollo.storytelling.CloseToJunction)
  ))
_sym_db.RegisterMessage(CloseToJunction)

CloseToSignal = _reflection.GeneratedProtocolMessageType('CloseToSignal', (_message.Message,), dict(
  DESCRIPTOR = _CLOSETOSIGNAL,
  __module__ = 'modules.storytelling.proto.story_pb2'
  # @@protoc_insertion_point(class_scope:apollo.storytelling.CloseToSignal)
  ))
_sym_db.RegisterMessage(CloseToSignal)

CloseToStopSign = _reflection.GeneratedProtocolMessageType('CloseToStopSign', (_message.Message,), dict(
  DESCRIPTOR = _CLOSETOSTOPSIGN,
  __module__ = 'modules.storytelling.proto.story_pb2'
  # @@protoc_insertion_point(class_scope:apollo.storytelling.CloseToStopSign)
  ))
_sym_db.RegisterMessage(CloseToStopSign)

CloseToYieldSign = _reflection.GeneratedProtocolMessageType('CloseToYieldSign', (_message.Message,), dict(
  DESCRIPTOR = _CLOSETOYIELDSIGN,
  __module__ = 'modules.storytelling.proto.story_pb2'
  # @@protoc_insertion_point(class_scope:apollo.storytelling.CloseToYieldSign)
  ))
_sym_db.RegisterMessage(CloseToYieldSign)

Stories = _reflection.GeneratedProtocolMessageType('Stories', (_message.Message,), dict(
  DESCRIPTOR = _STORIES,
  __module__ = 'modules.storytelling.proto.story_pb2'
  # @@protoc_insertion_point(class_scope:apollo.storytelling.Stories)
  ))
_sym_db.RegisterMessage(Stories)


# @@protoc_insertion_point(module_scope)
