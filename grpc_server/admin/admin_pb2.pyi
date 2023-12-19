from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Admin(_message.Message):
    __slots__ = ("id", "nip", "nama", "tgl_lahir", "alamat", "kontak", "email", "password")
    ID_FIELD_NUMBER: _ClassVar[int]
    NIP_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    TGL_LAHIR_FIELD_NUMBER: _ClassVar[int]
    ALAMAT_FIELD_NUMBER: _ClassVar[int]
    KONTAK_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    id: int
    nip: str
    nama: str
    tgl_lahir: str
    alamat: str
    kontak: str
    email: str
    password: str
    def __init__(self, id: _Optional[int] = ..., nip: _Optional[str] = ..., nama: _Optional[str] = ..., tgl_lahir: _Optional[str] = ..., alamat: _Optional[str] = ..., kontak: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AdminListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AdminListResponse(_message.Message):
    __slots__ = ("data", "message")
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Admin]
    message: str
    def __init__(self, data: _Optional[_Iterable[_Union[Admin, _Mapping]]] = ..., message: _Optional[str] = ...) -> None: ...

class AdminRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class AdminResponse(_message.Message):
    __slots__ = ("data", "message")
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    data: Admin
    message: str
    def __init__(self, data: _Optional[_Union[Admin, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class AdminCreateRequest(_message.Message):
    __slots__ = ("nip", "nama", "tgl_lahir", "alamat", "kontak", "email", "password")
    NIP_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    TGL_LAHIR_FIELD_NUMBER: _ClassVar[int]
    ALAMAT_FIELD_NUMBER: _ClassVar[int]
    KONTAK_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    nip: str
    nama: str
    tgl_lahir: str
    alamat: str
    kontak: str
    email: str
    password: str
    def __init__(self, nip: _Optional[str] = ..., nama: _Optional[str] = ..., tgl_lahir: _Optional[str] = ..., alamat: _Optional[str] = ..., kontak: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AdminUpdateRequest(_message.Message):
    __slots__ = ("nama", "tgl_lahir", "alamat", "kontak", "email", "password")
    NAMA_FIELD_NUMBER: _ClassVar[int]
    TGL_LAHIR_FIELD_NUMBER: _ClassVar[int]
    ALAMAT_FIELD_NUMBER: _ClassVar[int]
    KONTAK_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    nama: str
    tgl_lahir: str
    alamat: str
    kontak: str
    email: str
    password: str
    def __init__(self, nama: _Optional[str] = ..., tgl_lahir: _Optional[str] = ..., alamat: _Optional[str] = ..., kontak: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AdminDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class AdminDeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class AdminLoginRequest(_message.Message):
    __slots__ = ("nip", "password")
    NIP_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    nip: str
    password: str
    def __init__(self, nip: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AdminLoginResponse(_message.Message):
    __slots__ = ("message", "token")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    message: str
    token: str
    def __init__(self, message: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class AdminLogoutRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class AdminLogoutResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
