# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='server.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cserver.proto\"\x18\n\x07Request\x12\r\n\x05\x64\x61tas\x18\x01 \x01(\x0c\"\x13\n\x05Reply\x12\n\n\x02id\x18\x01 \x01(\x05\x32\x32\n\x0b\x46\x61\x63\x65Service\x12#\n\tgetStream\x12\x08.Request\x1a\x06.Reply\"\x00(\x01\x30\x01\x62\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='datas', full_name='Request.datas', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=40,
)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Reply.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=61,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:Reply)
  })
_sym_db.RegisterMessage(Reply)



_FACESERVICE = _descriptor.ServiceDescriptor(
  name='FaceService',
  full_name='FaceService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=63,
  serialized_end=113,
  methods=[
  _descriptor.MethodDescriptor(
    name='getStream',
    full_name='FaceService.getStream',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_REPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FACESERVICE)

DESCRIPTOR.services_by_name['FaceService'] = _FACESERVICE

# @@protoc_insertion_point(module_scope)
