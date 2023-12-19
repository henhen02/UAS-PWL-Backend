        # sa.Column('id', sa.Integer, primary_key=True),
        # sa.Column('nip', sa.String(length=18), nullable=False, unique=True),
        # sa.Column('nama', sa.String(length=50), nullable=False),
        # sa.Column('tgl_lahir', sa.Date, nullable=False),
        # sa.Column('alamat', sa.String(length=100), nullable=False),
        # sa.Column('kontak', sa.String(length=20), nullable=False),
        # sa.Column('email', sa.String(length=50), nullable=False, unique=True),
        # sa.Column('password', sa.String(length=100), nullable=False),
        # sa.Column('token', sa.String(length=100), nullable=True),

from sqlalchemy.orm import mapped_column, Mapped
from .meta import Base

class Admin(Base):
    __tablename__ = 'admin'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nip: Mapped[str] = mapped_column(nullable=False, unique=True)
    nama: Mapped[str] = mapped_column(nullable=False)
    tgl_lahir: Mapped[str] = mapped_column(nullable=False)
    alamat: Mapped[str] = mapped_column(nullable=False)
    kontak: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)   
    token: Mapped[str] = mapped_column(nullable=True)