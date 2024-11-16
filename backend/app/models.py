from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ChartData(Base):
    __tablename__ = "chart_data"
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, index=True)
    value = Column(Float)
