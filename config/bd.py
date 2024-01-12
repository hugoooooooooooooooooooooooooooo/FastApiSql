from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv,find_dotenv
import os

meta = MetaData()

load_dotenv(find_dotenv())
usuario = os.environ.get("USUARIO")
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")
bd = os.environ.get("BD")

engine = create_engine(f"mysql+pymysql://{usuario}:{password}@{host}/{bd}")

conn = engine.connect();

