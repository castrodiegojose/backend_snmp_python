from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.getenv('DB_CONNECTION'))
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'cm_models'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Model = Column(String(100))
    Vendor = Column(String(100))
    Softver = Column(String(100))

    def __init__(self, Model, Vendor, Softver):
        self.Model = Model
        self.Vendor = Vendor
        self.Softver = Softver

Base.metadata.create_all(engine)
