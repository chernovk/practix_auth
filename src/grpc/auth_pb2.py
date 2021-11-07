# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nauth.proto\"\x18\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\t\"B\n\rSignUpRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\")\n\x0eSignUpResponse\x12\x17\n\x06status\x18\x01 \x01(\x0b\x32\x07.Status\"3\n\rSignInRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"V\n\x0eSignInResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x17\n\x06status\x18\x03 \x01(\x0b\x32\x07.Status\"\'\n\x0eRefreshRequest\x12\x15\n\rrefresh_token\x18\x01 \x01(\t\"W\n\x0fRefreshResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x17\n\x06status\x18\x03 \x01(\x0b\x32\x07.Status\" \n\rLogoutRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\")\n\x0eLogoutResponse\x12\x17\n\x06status\x18\x01 \x01(\x0b\x32\x07.Status\"7\n\x11UserUpdateRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"-\n\x12UserUpdateResponse\x12\x17\n\x06status\x18\x01 \x01(\x0b\x32\x07.Status\",\n\x19GetUserAuthHistoryRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"I\n\x0fUserAuthHistory\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\nuser_agent\x18\x02 \x01(\t\x12\x11\n\tauth_date\x18\x03 \x01(\t\"?\n\x1aGetUserAuthHistoryResponse\x12!\n\x07history\x18\x01 \x03(\x0b\x32\x10.UserAuthHistory2\xbb\x02\n\x04\x41uth\x12)\n\x06SignUp\x12\x0e.SignUpRequest\x1a\x0f.SignUpResponse\x12)\n\x06SignIn\x12\x0e.SignInRequest\x1a\x0f.SignInResponse\x12,\n\x07Refresh\x12\x0f.RefreshRequest\x1a\x10.RefreshResponse\x12)\n\x06Logout\x12\x0e.LogoutRequest\x1a\x0f.LogoutResponse\x12\x35\n\nUserUpdate\x12\x12.UserUpdateRequest\x1a\x13.UserUpdateResponse\x12M\n\x12GetUserAuthHistory\x12\x1a.GetUserAuthHistoryRequest\x1a\x1b.GetUserAuthHistoryResponseb\x06proto3'
)




_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Status.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=14,
  serialized_end=38,
)


_SIGNUPREQUEST = _descriptor.Descriptor(
  name='SignUpRequest',
  full_name='SignUpRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='SignUpRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='SignUpRequest.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='SignUpRequest.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=40,
  serialized_end=106,
)


_SIGNUPRESPONSE = _descriptor.Descriptor(
  name='SignUpResponse',
  full_name='SignUpResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SignUpResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=108,
  serialized_end=149,
)


_SIGNINREQUEST = _descriptor.Descriptor(
  name='SignInRequest',
  full_name='SignInRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='SignInRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='SignInRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=151,
  serialized_end=202,
)


_SIGNINRESPONSE = _descriptor.Descriptor(
  name='SignInResponse',
  full_name='SignInResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='SignInResponse.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='refresh_token', full_name='SignInResponse.refresh_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='SignInResponse.status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=204,
  serialized_end=290,
)


_REFRESHREQUEST = _descriptor.Descriptor(
  name='RefreshRequest',
  full_name='RefreshRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='refresh_token', full_name='RefreshRequest.refresh_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=292,
  serialized_end=331,
)


_REFRESHRESPONSE = _descriptor.Descriptor(
  name='RefreshResponse',
  full_name='RefreshResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='RefreshResponse.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='refresh_token', full_name='RefreshResponse.refresh_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='RefreshResponse.status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=333,
  serialized_end=420,
)


_LOGOUTREQUEST = _descriptor.Descriptor(
  name='LogoutRequest',
  full_name='LogoutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='LogoutRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=422,
  serialized_end=454,
)


_LOGOUTRESPONSE = _descriptor.Descriptor(
  name='LogoutResponse',
  full_name='LogoutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='LogoutResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=456,
  serialized_end=497,
)


_USERUPDATEREQUEST = _descriptor.Descriptor(
  name='UserUpdateRequest',
  full_name='UserUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='UserUpdateRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='UserUpdateRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=499,
  serialized_end=554,
)


_USERUPDATERESPONSE = _descriptor.Descriptor(
  name='UserUpdateResponse',
  full_name='UserUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='UserUpdateResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=556,
  serialized_end=601,
)


_GETUSERAUTHHISTORYREQUEST = _descriptor.Descriptor(
  name='GetUserAuthHistoryRequest',
  full_name='GetUserAuthHistoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='GetUserAuthHistoryRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=603,
  serialized_end=647,
)


_USERAUTHHISTORY = _descriptor.Descriptor(
  name='UserAuthHistory',
  full_name='UserAuthHistory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='UserAuthHistory.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_agent', full_name='UserAuthHistory.user_agent', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auth_date', full_name='UserAuthHistory.auth_date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=649,
  serialized_end=722,
)


_GETUSERAUTHHISTORYRESPONSE = _descriptor.Descriptor(
  name='GetUserAuthHistoryResponse',
  full_name='GetUserAuthHistoryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='history', full_name='GetUserAuthHistoryResponse.history', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=724,
  serialized_end=787,
)

_SIGNUPRESPONSE.fields_by_name['status'].message_type = _STATUS
_SIGNINRESPONSE.fields_by_name['status'].message_type = _STATUS
_REFRESHRESPONSE.fields_by_name['status'].message_type = _STATUS
_LOGOUTRESPONSE.fields_by_name['status'].message_type = _STATUS
_USERUPDATERESPONSE.fields_by_name['status'].message_type = _STATUS
_GETUSERAUTHHISTORYRESPONSE.fields_by_name['history'].message_type = _USERAUTHHISTORY
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['SignUpRequest'] = _SIGNUPREQUEST
DESCRIPTOR.message_types_by_name['SignUpResponse'] = _SIGNUPRESPONSE
DESCRIPTOR.message_types_by_name['SignInRequest'] = _SIGNINREQUEST
DESCRIPTOR.message_types_by_name['SignInResponse'] = _SIGNINRESPONSE
DESCRIPTOR.message_types_by_name['RefreshRequest'] = _REFRESHREQUEST
DESCRIPTOR.message_types_by_name['RefreshResponse'] = _REFRESHRESPONSE
DESCRIPTOR.message_types_by_name['LogoutRequest'] = _LOGOUTREQUEST
DESCRIPTOR.message_types_by_name['LogoutResponse'] = _LOGOUTRESPONSE
DESCRIPTOR.message_types_by_name['UserUpdateRequest'] = _USERUPDATEREQUEST
DESCRIPTOR.message_types_by_name['UserUpdateResponse'] = _USERUPDATERESPONSE
DESCRIPTOR.message_types_by_name['GetUserAuthHistoryRequest'] = _GETUSERAUTHHISTORYREQUEST
DESCRIPTOR.message_types_by_name['UserAuthHistory'] = _USERAUTHHISTORY
DESCRIPTOR.message_types_by_name['GetUserAuthHistoryResponse'] = _GETUSERAUTHHISTORYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:Status)
  })
_sym_db.RegisterMessage(Status)

SignUpRequest = _reflection.GeneratedProtocolMessageType('SignUpRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPREQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:SignUpRequest)
  })
_sym_db.RegisterMessage(SignUpRequest)

SignUpResponse = _reflection.GeneratedProtocolMessageType('SignUpResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPRESPONSE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:SignUpResponse)
  })
_sym_db.RegisterMessage(SignUpResponse)

SignInRequest = _reflection.GeneratedProtocolMessageType('SignInRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNINREQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:SignInRequest)
  })
_sym_db.RegisterMessage(SignInRequest)

SignInResponse = _reflection.GeneratedProtocolMessageType('SignInResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIGNINRESPONSE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:SignInResponse)
  })
_sym_db.RegisterMessage(SignInResponse)

RefreshRequest = _reflection.GeneratedProtocolMessageType('RefreshRequest', (_message.Message,), {
  'DESCRIPTOR' : _REFRESHREQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:RefreshRequest)
  })
_sym_db.RegisterMessage(RefreshRequest)

RefreshResponse = _reflection.GeneratedProtocolMessageType('RefreshResponse', (_message.Message,), {
  'DESCRIPTOR' : _REFRESHRESPONSE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:RefreshResponse)
  })
_sym_db.RegisterMessage(RefreshResponse)

LogoutRequest = _reflection.GeneratedProtocolMessageType('LogoutRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGOUTREQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:LogoutRequest)
  })
_sym_db.RegisterMessage(LogoutRequest)

LogoutResponse = _reflection.GeneratedProtocolMessageType('LogoutResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGOUTRESPONSE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:LogoutResponse)
  })
_sym_db.RegisterMessage(LogoutResponse)

UserUpdateRequest = _reflection.GeneratedProtocolMessageType('UserUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERUPDATEREQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:UserUpdateRequest)
  })
_sym_db.RegisterMessage(UserUpdateRequest)

UserUpdateResponse = _reflection.GeneratedProtocolMessageType('UserUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERUPDATERESPONSE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:UserUpdateResponse)
  })
_sym_db.RegisterMessage(UserUpdateResponse)

GetUserAuthHistoryRequest = _reflection.GeneratedProtocolMessageType('GetUserAuthHistoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERAUTHHISTORYREQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:GetUserAuthHistoryRequest)
  })
_sym_db.RegisterMessage(GetUserAuthHistoryRequest)

UserAuthHistory = _reflection.GeneratedProtocolMessageType('UserAuthHistory', (_message.Message,), {
  'DESCRIPTOR' : _USERAUTHHISTORY,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:UserAuthHistory)
  })
_sym_db.RegisterMessage(UserAuthHistory)

GetUserAuthHistoryResponse = _reflection.GeneratedProtocolMessageType('GetUserAuthHistoryResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERAUTHHISTORYRESPONSE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:GetUserAuthHistoryResponse)
  })
_sym_db.RegisterMessage(GetUserAuthHistoryResponse)



_AUTH = _descriptor.ServiceDescriptor(
  name='Auth',
  full_name='Auth',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=790,
  serialized_end=1105,
  methods=[
  _descriptor.MethodDescriptor(
    name='SignUp',
    full_name='Auth.SignUp',
    index=0,
    containing_service=None,
    input_type=_SIGNUPREQUEST,
    output_type=_SIGNUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SignIn',
    full_name='Auth.SignIn',
    index=1,
    containing_service=None,
    input_type=_SIGNINREQUEST,
    output_type=_SIGNINRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Refresh',
    full_name='Auth.Refresh',
    index=2,
    containing_service=None,
    input_type=_REFRESHREQUEST,
    output_type=_REFRESHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Logout',
    full_name='Auth.Logout',
    index=3,
    containing_service=None,
    input_type=_LOGOUTREQUEST,
    output_type=_LOGOUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UserUpdate',
    full_name='Auth.UserUpdate',
    index=4,
    containing_service=None,
    input_type=_USERUPDATEREQUEST,
    output_type=_USERUPDATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserAuthHistory',
    full_name='Auth.GetUserAuthHistory',
    index=5,
    containing_service=None,
    input_type=_GETUSERAUTHHISTORYREQUEST,
    output_type=_GETUSERAUTHHISTORYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTH)

DESCRIPTOR.services_by_name['Auth'] = _AUTH

# @@protoc_insertion_point(module_scope)
