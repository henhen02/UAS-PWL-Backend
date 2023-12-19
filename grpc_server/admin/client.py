import admin_pb2_grpc
import admin_pb2
import grpc

class AdminClient:
    def __init__(self):
        self.localhost = 'localhost'
        self.port = '8001'
        self.channel = grpc.insecure_channel(self.localhost + ':' + self.port)
        self.stub = admin_pb2_grpc.AdminServiceStub(self.channel)

    def Login(self, nip, password):
        
        response = self.stub.Login(admin_pb2.AdminLoginRequest(nip=nip, password=password))
        if response is None:
            return None
        
        return [
            dict(
                message=response.message,
                token=response.token
            )
        ]
    
    def Logout(self, token):
        response = self.stub.Logout(admin_pb2.AdminLogoutRequest(token=token))
        if response is None:
            return None
        
        return [
            dict(
                message=response.message
            )
        ]

if __name__ == '__main__':
    admin = AdminClient()
    res = admin.Login('SYS.210120022201', 'admin')
    print(res)