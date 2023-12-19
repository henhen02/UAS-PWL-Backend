from concurrent import futures
import time
import grpc
import admin_pb2
import admin_pb2_grpc
import logging
import jwt
import traceback

from database.config import engine
from sqlalchemy import insert, select, update, desc, delete
from model.admin import Admin

class AdminServices(admin_pb2_grpc.AdminServiceServicer):
    def Login(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                query = select(Admin).where(Admin.nip == request.nip)
                result = conn.execute(query).first()
                conn.commit()
                
                print(result)

                if result is None:
                    return admin_pb2.AdminLoginResponse(
                        message="NIP tidak ditemukan",
                        token=""
                    )
                if result[7] != request.password:
                    return admin_pb2.AdminLoginResponse(
                        message="Password salah",
                        token=""
                    )
                conn.begin()
                token = jwt.encode({
                    'nip': request.nip,
                },
                'secret', algorithm='HS256')
                query = update(Admin).where(Admin.nip == request.nip).values(token=token)
                conn.execute(query)
                conn.commit()

                return admin_pb2.AdminLoginResponse(
                    message="Login berhasil",
                    token=token
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)

            return admin_pb2.AdminLoginResponse(
                message="Terjadi kesalahan pada server",
                token=""
            )
    
    def Logout(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                decode = jwt.decode(request.token, 'secret', algorithms=['HS256'])
                query = update(Admin).where(Admin.nip == decode['nip']).values(token="")
                result = conn.execute(query).first()
                if result is None:
                    return admin_pb2.AdminLogoutResponse(
                        message=""
                    )
                conn.commit()

                return admin_pb2.AdminLogoutResponse(
                    message="Logout berhasil"
                )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return admin_pb2.AdminLogoutResponse(
                message="Terjadi kesalahan pada server"
            )
                
def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    admin_pb2_grpc.add_AdminServiceServicer_to_server(AdminServices(), server)
    server.add_insecure_port('localhost:8001')
    server.start()
    print("Server running at localhost:8001")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    server()