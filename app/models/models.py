from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey, String
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP, BYTEA

metadata = MetaData()

questions = Table(
    'questions',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('question', String, nullable=False),
    Column('answer', String, nullable=False),
    Column('created_at', TIMESTAMP, nullable=False)
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('uuid', UUID, nullable=False),
    Column('created_at', TIMESTAMP, default=datetime.utcnow),
)

media = Table(
    'media',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('audio', BYTEA, nullable=False)
)
