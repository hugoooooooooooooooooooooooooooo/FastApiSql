from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer,String,Float
from config.bd import meta, engine

platos = Table(
    "platosApi",
    meta, 
    Column("id",Integer, primary_key=True),
    Column('nombre', String(100)),
    Column('precio', Float),
    Column('tipo', String(20)),
)
meta.create_all(engine, checkfirst=True)

