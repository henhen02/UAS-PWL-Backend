"""initial commit

Revision ID: d351350bd133
Revises: 
Create Date: 2023-12-19 06:41:50.176411

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd351350bd133'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # string id = 1;
    # string nip = 2;
    # string nama = 3;
    # string tgl_lahir = 4;
    # string alamat = 5;
    # string kontak = 6;
    # string email = 7;
    # string password = 7;
    op.create_table(
        'admin',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nip', sa.String(length=18), nullable=False, unique=True),
        sa.Column('nama', sa.String(length=50), nullable=False),
        sa.Column('tgl_lahir', sa.Date, nullable=False),
        sa.Column('alamat', sa.String(length=100), nullable=False),
        sa.Column('kontak', sa.String(length=20), nullable=False),
        sa.Column('email', sa.String(length=50), nullable=False, unique=True),
        sa.Column('password', sa.String(length=100), nullable=False),
        sa.Column('token', sa.String(length=100), nullable=True),
        
    )

    # string id = 1;
    # string nip = 2;
    # string nama = 3;
    # string tgl_lahir = 4;
    # string kontak = 5;
    # string email = 6;
    # string alamat = 7;
    op.create_table(
        'petugas',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nip', sa.String(length=18), nullable=False, unique=True),
        sa.Column('nama', sa.String(length=50), nullable=False),
        sa.Column('tgl_lahir', sa.Date, nullable=False),
        sa.Column('kontak', sa.String(length=20), nullable=False),
        sa.Column('email', sa.String(length=50), nullable=False, unique=True),
        sa.Column('alamat', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_table(
        'jenis_sampling',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('nama', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )

    # string id = 1;
    # string instansi = 2;
    # string alamat = 3;
    # string tanggal = 4;
    # repeated string petugas_id = 5;
    # string penanggung_jawab = 6;
    # string kontak_penanggung_jawab = 7;
    # bool status_id = 8;
    # string jenis_sampling_id = 9;
    op.create_table(
        'jadwal_sampling',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('instansi', sa.String(length=50), nullable=False),
        sa.Column('alamat', sa.String(length=255), nullable=False),
        sa.Column('tanggal', sa.Date, nullable=False),
        sa.Column('petugas_id', sa.Integer, nullable=False),
        sa.Column('penanggung_jawab', sa.String(length=50), nullable=False),
        sa.Column('kontak_penanggung_jawab', sa.String(length=20), nullable=False),
        sa.Column('status', sa.Integer, nullable=False, default=0),
        sa.Column('jenis_sampling_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['petugas_id'], ['petugas.id'], name='fk_jadwal_sampling_petugas_id', ondelete='CASCADE', onupdate='CASCADE' ),
        sa.ForeignKeyConstraint(['jenis_sampling_id'], ['jenis_sampling.id'], name='fk_jadwal_sampling_jenis_sampling_id', ondelete='CASCADE', onupdate='CASCADE' ),
    )


    op.bulk_insert(
        sa.table('jenis_sampling',     
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('nama', sa.String(length=50), nullable=False),
        ),
        [
            {'id': 1, 'nama': 'Air Bersih'},
            {'id': 2, 'nama': 'Air Limbah'},
            {'id': 3, 'nama': 'Air Sungai'},
            {'id': 4, 'nama': 'Kebisingan'},
            {'id': 5, 'nama': 'Getaran'},
            {'id': 6, 'nama': 'Udara'},
            {'id': 7, 'nama': 'Polusi'},
            {'id': 8, 'nama': 'Cahaya'},
        ]
    )

    op.bulk_insert(
        sa.table('petugas',         
            sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
            sa.Column('nip', sa.String(length=18), nullable=False, unique=True),
            sa.Column('nama', sa.String(length=50), nullable=False),
            sa.Column('tgl_lahir', sa.Date, nullable=False),
            sa.Column('kontak', sa.String(length=20), nullable=False),
            sa.Column('email', sa.String(length=50), nullable=False, unique=True),
            sa.Column('alamat', sa.String(length=255), nullable=False),
        ),
        [
            {
                'id': 1,
                'nip': 'SYS.210720022202',
                'nama': 'Hendri Aldi Zulfan',
                'tgl_lahir': '2002-07-21',
                'kontak': '085789418464',
                'email': 'hendrialdizulfan@gmail.com',
                'alamat': 'Palem Asri Blok D No. 1, Kelurahan Way Kandis, Kecamatan Tanjung Senang, Bandar Lampung',
            },
            {
                'id': 2,
                'nip': 'SYS.210220022203',
                'nama': 'Bagus Ardin Saputra',
                'tgl_lahir': '2002-02-21',
                'kontak': '085789888464',
                'email': 'bagusardin@gmail.com',
                'alamat': 'Palem Asri Blok D No. 2, Kelurahan Way Kandis, Kecamatan Tanjung Senang, Bandar Lampung',
            },
        ]
    )

    op.bulk_insert(
        sa.table('admin',         
            sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
            sa.Column('nip', sa.String(length=18), nullable=False, unique=True),
            sa.Column('nama', sa.String(length=50), nullable=False),
            sa.Column('tgl_lahir', sa.Date, nullable=False),
            sa.Column('kontak', sa.String(length=20), nullable=False),
            sa.Column('email', sa.String(length=50), nullable=False, unique=True),
            sa.Column('alamat', sa.String(length=255), nullable=False),
            sa.Column('password', sa.String(length=100), nullable=False),
            sa.Column('token', sa.String(length=100), nullable=True),
        ),
        [
            {
                'nip': 'SYS.210120022201',
                'nama': 'Admin',
                'tgl_lahir': '2002-01-21',
                'kontak': '085789888464',
                'email': 'admin@gmail.com',
                'alamat': 'Palem Asri Blok D No. 2, Kelurahan Way Kandis, Kecamatan Tanjung Senang, Bandar Lampung',
                'password': 'admin',
                'token': '',
            },
        ]
    )

    op.bulk_insert(
        sa.table('jadwal_sampling',         
            sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
            sa.Column('instansi', sa.String(length=50), nullable=False),
            sa.Column('alamat', sa.String(length=255), nullable=False),
            sa.Column('tanggal', sa.Date, nullable=False),
            sa.Column('petugas_id', sa.String(length=36), nullable=False),
            sa.Column('penanggung_jawab', sa.String(length=50), nullable=False),
            sa.Column('kontak_penanggung_jawab', sa.String(length=20), nullable=False),
            sa.Column('status', sa.Integer, nullable=False, default=0),
            sa.Column('jenis_sampling_id', sa.Integer, nullable=False),
        ),
        [
            {
                'instansi': 'PT. PLN (Persero) Distribusi Lampung',
                'alamat': 'Jl. Raden Intan No. 1, Bandar Lampung',
                'tanggal': '2021-07-21',
                'petugas_id': 1,
                'penanggung_jawab': 'Hendri Aldi Zulfan',
                'kontak_penanggung_jawab': '085789418464',
                'status': 0,
                'jenis_sampling_id': 1,
            },
            {
                'instansi': 'PT. PLN (Persero) Distribusi Lampung',
                'alamat': 'Jl. Raden Intan No. 1, Bandar Lampung',
                'tanggal': '2021-07-21',
                'petugas_id': 2,
                'penanggung_jawab': 'Bagus Ardin Saputra',
                'kontak_penanggung_jawab': '085789888464',
                'status': 0,
                'jenis_sampling_id': 2,
            },
        ]
    )


def downgrade() -> None:
    pass
