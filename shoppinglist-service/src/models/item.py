from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer)
    checked = Column(Boolean, default=False)
