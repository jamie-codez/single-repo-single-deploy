from sqlalchemy import (Column,Integer,String,MetaData,Table,create_engine,ARRAY)
from databases import Database
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name",String(50)),
    Column("plot",String(100)),
    Column("genres",ARRAY(String)),
    Column("casts_id",ARRAY(Integer))
)

database = Database(DATABASE_URL)