from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Table, String, Integer
from database import engine

class Model(DeclarativeBase):
    pass

class TaskOrm(Model):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)