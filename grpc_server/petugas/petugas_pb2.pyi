from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Petugas(_message.Message):
    __slots__ = ("id", "nip", "nama", "tgl_lahir", "kontak", "email", "alamat")
    ID_FIELD_NUMBER: _ClassVar[int]
    NIP_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    TGL_LAHIR_FIELD_NUMBER: _ClassVar[int]
    KONTAK_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ALAMAT_FIELD_NUMBER: _ClassVar[int]
    id: int
    nip: str
    nama: str
    tgl_lahir: str
    kontak: str
    email: str
    alamat: str
    def __init__(self, id: _Optional[int] = ..., nip: _Optional[str] = ..., nama: _Optional[str] = ..., tgl_lahir: _Optional[str] = ..., kontak: _Optional[str] = ..., email: _Optional[str] = ..., alamat: _Optional[str] = ...) -> None: ...

class CreatePetugasRequest(_message.Message):
    __slots__ = ("nip", "nama", "tgl_lahir", "kontak", "email", "alamat")
    NIP_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    TGL_LAHIR_FIELD_NUMBER: _ClassVar[int]
    KONTAK_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ALAMAT_FIELD_NUMBER: _ClassVar[int]
    nip: str
    nama: str
    tgl_lahir: str
    kontak: str
    email: str
    alamat: str
    def __init__(self, nip: _Optional[str] = ..., nama: _Optional[str] = ..., tgl_lahir: _Optional[str] = ..., kontak: _Optional[str] = ..., email: _Optional[str] = ..., alamat: _Optional[str] = ...) -> None: ...

class PetugasListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PetugasListResponse(_message.Message):
    __slots__ = ("data", "message")
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Petugas]
    message: str
    def __init__(self, data: _Optional[_Iterable[_Union[Petugas, _Mapping]]] = ..., message: _Optional[str] = ...) -> None: ...

class PetugasRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class PetugasResponse(_message.Message):
    __slots__ = ("data", "message")
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    data: Petugas
    message: str
    def __init__(self, data: _Optional[_Union[Petugas, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class UpdatePetugasRequest(_message.Message):
    __slots__ = ("nama", "tgl_lahir", "kontak", "email", "alamat")
    NAMA_FIELD_NUMBER: _ClassVar[int]
    TGL_LAHIR_FIELD_NUMBER: _ClassVar[int]
    KONTAK_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ALAMAT_FIELD_NUMBER: _ClassVar[int]
    nama: str
    tgl_lahir: str
    kontak: str
    email: str
    alamat: str
    def __init__(self, nama: _Optional[str] = ..., tgl_lahir: _Optional[str] = ..., kontak: _Optional[str] = ..., email: _Optional[str] = ..., alamat: _Optional[str] = ...) -> None: ...

class DeletePetugasRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeletePetugasResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class LoginPetugasRequest(_message.Message):
    __slots__ = ("nip",)
    NIP_FIELD_NUMBER: _ClassVar[int]
    nip: str
    def __init__(self, nip: _Optional[str] = ...) -> None: ...

class LoginPetugasResponse(_message.Message):
    __slots__ = ("data", "message")
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    data: Petugas
    message: str
    def __init__(self, data: _Optional[_Union[Petugas, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...
