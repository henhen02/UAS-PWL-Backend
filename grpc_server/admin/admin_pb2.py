# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admin.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61\x64min.proto\x12\x05\x61\x64min\"\x82\x01\n\x05\x41\x64min\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0b\n\x03nip\x18\x02 \x01(\t\x12\x0c\n\x04nama\x18\x03 \x01(\t\x12\x11\n\ttgl_lahir\x18\x04 \x01(\t\x12\x0e\n\x06\x61lamat\x18\x05 \x01(\t\x12\x0e\n\x06kontak\x18\x06 \x01(\t\x12\r\n\x05\x65mail\x18\x07 \x01(\t\x12\x10\n\x08password\x18\x08 \x01(\t\"\x12\n\x10\x41\x64minListRequest\"@\n\x11\x41\x64minListResponse\x12\x1a\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x0c.admin.Admin\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1a\n\x0c\x41\x64minRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"<\n\rAdminResponse\x12\x1a\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x0c.admin.Admin\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x83\x01\n\x12\x41\x64minCreateRequest\x12\x0b\n\x03nip\x18\x01 \x01(\t\x12\x0c\n\x04nama\x18\x02 \x01(\t\x12\x11\n\ttgl_lahir\x18\x03 \x01(\t\x12\x0e\n\x06\x61lamat\x18\x04 \x01(\t\x12\x0e\n\x06kontak\x18\x05 \x01(\t\x12\r\n\x05\x65mail\x18\x06 \x01(\t\x12\x10\n\x08password\x18\x07 \x01(\t\"v\n\x12\x41\x64minUpdateRequest\x12\x0c\n\x04nama\x18\x01 \x01(\t\x12\x11\n\ttgl_lahir\x18\x02 \x01(\t\x12\x0e\n\x06\x61lamat\x18\x03 \x01(\t\x12\x0e\n\x06kontak\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x10\n\x08password\x18\x06 \x01(\t\" \n\x12\x41\x64minDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"&\n\x13\x41\x64minDeleteResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"2\n\x11\x41\x64minLoginRequest\x12\x0b\n\x03nip\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"4\n\x12\x41\x64minLoginResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"#\n\x12\x41\x64minLogoutRequest\x12\r\n\x05token\x18\x01 \x01(\t\"&\n\x13\x41\x64minLogoutResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xb1\x03\n\x0c\x41\x64minService\x12\x39\n\x04List\x12\x17.admin.AdminListRequest\x1a\x18.admin.AdminListResponse\x12\x30\n\x03Get\x12\x13.admin.AdminRequest\x1a\x14.admin.AdminResponse\x12\x39\n\x06\x43reate\x12\x19.admin.AdminCreateRequest\x1a\x14.admin.AdminResponse\x12\x39\n\x06Update\x12\x19.admin.AdminUpdateRequest\x1a\x14.admin.AdminResponse\x12?\n\x06\x44\x65lete\x12\x19.admin.AdminDeleteRequest\x1a\x1a.admin.AdminDeleteResponse\x12<\n\x05Login\x12\x18.admin.AdminLoginRequest\x1a\x19.admin.AdminLoginResponse\x12?\n\x06Logout\x12\x19.admin.AdminLogoutRequest\x1a\x1a.admin.AdminLogoutResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'admin_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ADMIN']._serialized_start=23
  _globals['_ADMIN']._serialized_end=153
  _globals['_ADMINLISTREQUEST']._serialized_start=155
  _globals['_ADMINLISTREQUEST']._serialized_end=173
  _globals['_ADMINLISTRESPONSE']._serialized_start=175
  _globals['_ADMINLISTRESPONSE']._serialized_end=239
  _globals['_ADMINREQUEST']._serialized_start=241
  _globals['_ADMINREQUEST']._serialized_end=267
  _globals['_ADMINRESPONSE']._serialized_start=269
  _globals['_ADMINRESPONSE']._serialized_end=329
  _globals['_ADMINCREATEREQUEST']._serialized_start=332
  _globals['_ADMINCREATEREQUEST']._serialized_end=463
  _globals['_ADMINUPDATEREQUEST']._serialized_start=465
  _globals['_ADMINUPDATEREQUEST']._serialized_end=583
  _globals['_ADMINDELETEREQUEST']._serialized_start=585
  _globals['_ADMINDELETEREQUEST']._serialized_end=617
  _globals['_ADMINDELETERESPONSE']._serialized_start=619
  _globals['_ADMINDELETERESPONSE']._serialized_end=657
  _globals['_ADMINLOGINREQUEST']._serialized_start=659
  _globals['_ADMINLOGINREQUEST']._serialized_end=709
  _globals['_ADMINLOGINRESPONSE']._serialized_start=711
  _globals['_ADMINLOGINRESPONSE']._serialized_end=763
  _globals['_ADMINLOGOUTREQUEST']._serialized_start=765
  _globals['_ADMINLOGOUTREQUEST']._serialized_end=800
  _globals['_ADMINLOGOUTRESPONSE']._serialized_start=802
  _globals['_ADMINLOGOUTRESPONSE']._serialized_end=840
  _globals['_ADMINSERVICE']._serialized_start=843
  _globals['_ADMINSERVICE']._serialized_end=1276
# @@protoc_insertion_point(module_scope)