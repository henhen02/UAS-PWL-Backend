./env/Scripts/activate.bat

./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/admin --pyi_out=./grpc_server/admin --grpc_python_out=./grpc_server/admin ./grpc/admin.proto

./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/petugas --pyi_out=./grpc_server/petugas --grpc_python_out=./grpc_server/petugas ./grpc/petugas.proto

./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/penjadwalan --pyi_out=./grpc_server/penjadwalan --grpc_python_out=./grpc_server/penjadwalan ./grpc/penjadwalan.proto
