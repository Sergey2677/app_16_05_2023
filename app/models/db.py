from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey, String, create_engine
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP, BYTEA
from databases import Database
from config import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# SQLAlchemy
engine = create_engine(DATABASE_URL)

metadata = MetaData()

questions = Table(
    'questions',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('question_id', Integer, nullable=False),
    Column('question', String, nullable=False),
    Column('answer', String, nullable=False),
    Column('created_at', String, nullable=False)
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('uuid', UUID, nullable=False),
    Column('created_at', TIMESTAMP, default=datetime.utcnow),
)

media = Table(
    'media',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('audio', BYTEA, nullable=False)
)

database = Database(DATABASE_URL)
