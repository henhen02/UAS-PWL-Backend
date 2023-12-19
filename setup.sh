python3 -m venv env

./env/Scripts/activate

./env/Scripts/pip install -e .

./env/Scripts/alembic init alembic

./env/Scripts/alembic revision -m "Initial migration"

./env/Scripts/alembic upgrade head

cd grpc_server

python3 -m venv ./admin/env

./admin/env/Scripts/activate.bat

./admin/env/Scripts/pip install -e ./admin

python3 -m venv ./penjadwalan/env

./penjadwalan/env/Scripts/activate.bat

./penjadwalan/env/Scripts/pip install -e ./penjadwalan

python3 -m venv ./petugas/env

./petugas/env/Scripts/activate.bat

./petugas/env/Scripts/pip install -e ./petugas
