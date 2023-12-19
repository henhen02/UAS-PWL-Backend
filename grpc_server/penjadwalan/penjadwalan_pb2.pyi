from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Jadwal(_message.Message):
    __slots__ = ("id", "instansi", "alamat", "tanggal", "petugas_id", "penanggung_jawab", "kontak_penanggung_jawab", "status", "jenis_sampling_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    INSTANSI_FIELD_NUMBER: _ClassVar[int]
    ALAMAT_FIELD_NUMBER: _ClassVar[int]
    TANGGAL_FIELD_NUMBER: _ClassVar[int]
    PETUGAS_ID_FIELD_NUMBER: _ClassVar[int]
    PENANGGUNG_JAWAB_FIELD_NUMBER: _ClassVar[int]
    KONTAK_PENANGGUNG_JAWAB_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JENIS_SAMPLING_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    instansi: str
    alamat: str
    tanggal: str
    petugas_id: _containers.RepeatedScalarFieldContainer[str]
    penanggung_jawab: str
    kontak_penanggung_jawab: str
    status: int
    jenis_sampling_id: str
    def __init__(self, id: _Optional[int] = ..., instansi: _Optional[str] = ..., alamat: _Optional[str] = ..., tanggal: _Optional[str] = ..., petugas_id: _Optional[_Iterable[str]] = ..., penanggung_jawab: _Optional[str] = ..., kontak_penanggung_jawab: _Optional[str] = ..., status: _Optional[int] = ..., jenis_sampling_id: _Optional[str] = ...) -> None: ...

class JadwalListResponse(_message.Message):
    __slots__ = ("data", "message")
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Jadwal]
    message: str
    def __init__(self, data: _Optional[_Iterable[_Union[Jadwal, _Mapping]]] = ..., message: _Optional[str] = ...) -> None: ...

class JadwalListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JadwalResponse(_message.Message):
    __slots__ = ("data", "message")
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    data: Jadwal
    message: str
    def __init__(self, data: _Optional[_Union[Jadwal, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class JadwalRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class CreateJadwalRequest(_message.Message):
    __slots__ = ("instansi", "alamat", "tanggal", "petugas_id", "penanggung_jawab", "kontak_penanggung_jawab", "status", "jenis_sampling_id")
    INSTANSI_FIELD_NUMBER: _ClassVar[int]
    ALAMAT_FIELD_NUMBER: _ClassVar[int]
    TANGGAL_FIELD_NUMBER: _ClassVar[int]
    PETUGAS_ID_FIELD_NUMBER: _ClassVar[int]
    PENANGGUNG_JAWAB_FIELD_NUMBER: _ClassVar[int]
    KONTAK_PENANGGUNG_JAWAB_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JENIS_SAMPLING_ID_FIELD_NUMBER: _ClassVar[int]
    instansi: str
    alamat: str
    tanggal: str
    petugas_id: _containers.RepeatedScalarFieldContainer[str]
    penanggung_jawab: str
    kontak_penanggung_jawab: str
    status: int
    jenis_sampling_id: str
    def __init__(self, instansi: _Optional[str] = ..., alamat: _Optional[str] = ..., tanggal: _Optional[str] = ..., petugas_id: _Optional[_Iterable[str]] = ..., penanggung_jawab: _Optional[str] = ..., kontak_penanggung_jawab: _Optional[str] = ..., status: _Optional[int] = ..., jenis_sampling_id: _Optional[str] = ...) -> None: ...

class DeleteJadwalResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class DeleteJadwalRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
