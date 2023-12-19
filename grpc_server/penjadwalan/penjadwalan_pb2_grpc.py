# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import penjadwalan_pb2 as penjadwalan__pb2


class JadwalServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetJadwalList = channel.unary_unary(
                '/penjadwalan.JadwalService/GetJadwalList',
                request_serializer=penjadwalan__pb2.JadwalListRequest.SerializeToString,
                response_deserializer=penjadwalan__pb2.JadwalListResponse.FromString,
                )
        self.GetJadwal = channel.unary_unary(
                '/penjadwalan.JadwalService/GetJadwal',
                request_serializer=penjadwalan__pb2.JadwalRequest.SerializeToString,
                response_deserializer=penjadwalan__pb2.JadwalResponse.FromString,
                )
        self.CreateJadwal = channel.unary_unary(
                '/penjadwalan.JadwalService/CreateJadwal',
                request_serializer=penjadwalan__pb2.CreateJadwalRequest.SerializeToString,
                response_deserializer=penjadwalan__pb2.JadwalResponse.FromString,
                )
        self.DeleteJadwal = channel.unary_unary(
                '/penjadwalan.JadwalService/DeleteJadwal',
                request_serializer=penjadwalan__pb2.DeleteJadwalRequest.SerializeToString,
                response_deserializer=penjadwalan__pb2.DeleteJadwalResponse.FromString,
                )


class JadwalServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetJadwalList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJadwal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateJadwal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteJadwal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JadwalServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetJadwalList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJadwalList,
                    request_deserializer=penjadwalan__pb2.JadwalListRequest.FromString,
                    response_serializer=penjadwalan__pb2.JadwalListResponse.SerializeToString,
            ),
            'GetJadwal': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJadwal,
                    request_deserializer=penjadwalan__pb2.JadwalRequest.FromString,
                    response_serializer=penjadwalan__pb2.JadwalResponse.SerializeToString,
            ),
            'CreateJadwal': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateJadwal,
                    request_deserializer=penjadwalan__pb2.CreateJadwalRequest.FromString,
                    response_serializer=penjadwalan__pb2.JadwalResponse.SerializeToString,
            ),
            'DeleteJadwal': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteJadwal,
                    request_deserializer=penjadwalan__pb2.DeleteJadwalRequest.FromString,
                    response_serializer=penjadwalan__pb2.DeleteJadwalResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'penjadwalan.JadwalService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JadwalService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetJadwalList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/penjadwalan.JadwalService/GetJadwalList',
            penjadwalan__pb2.JadwalListRequest.SerializeToString,
            penjadwalan__pb2.JadwalListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJadwal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/penjadwalan.JadwalService/GetJadwal',
            penjadwalan__pb2.JadwalRequest.SerializeToString,
            penjadwalan__pb2.JadwalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateJadwal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/penjadwalan.JadwalService/CreateJadwal',
            penjadwalan__pb2.CreateJadwalRequest.SerializeToString,
            penjadwalan__pb2.JadwalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteJadwal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/penjadwalan.JadwalService/DeleteJadwal',
            penjadwalan__pb2.DeleteJadwalRequest.SerializeToString,
            penjadwalan__pb2.DeleteJadwalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
