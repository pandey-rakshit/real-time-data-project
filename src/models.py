from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    item = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.now)


# SQLite database connection
engine = create_engine("sqlite:///db/sqlite.db")
Base.metadata.create_all(engine)

# Session setup
Session = sessionmaker(bind=engine)
session = Session()
