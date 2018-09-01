# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/stats/game_stats.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...api.stats import events_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/stats/game_stats.proto',
  package='api.stats',
  serialized_pb=_b('\n\x1a\x61pi/stats/game_stats.proto\x12\tapi.stats\x1a\x16\x61pi/stats/events.proto\"j\n\tGameStats\x12\x1c\n\x04hits\x18\x01 \x03(\x0b\x32\x0e.api.stats.Hit\x12\x1f\n\x17neutral_possession_time\x18\x02 \x01(\x02\x12\x1e\n\x05\x62umps\x18\x03 \x03(\x0b\x32\x0f.api.stats.Bump')
  ,
  dependencies=[events_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GAMESTATS = _descriptor.Descriptor(
  name='GameStats',
  full_name='api.stats.GameStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hits', full_name='api.stats.GameStats.hits', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='neutral_possession_time', full_name='api.stats.GameStats.neutral_possession_time', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bumps', full_name='api.stats.GameStats.bumps', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=171,
)

_GAMESTATS.fields_by_name['hits'].message_type = events_pb2._HIT
_GAMESTATS.fields_by_name['bumps'].message_type = events_pb2._BUMP
DESCRIPTOR.message_types_by_name['GameStats'] = _GAMESTATS

GameStats = _reflection.GeneratedProtocolMessageType('GameStats', (_message.Message,), dict(
  DESCRIPTOR = _GAMESTATS,
  __module__ = 'api.stats.game_stats_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.GameStats)
  ))
_sym_db.RegisterMessage(GameStats)


# @@protoc_insertion_point(module_scope)
