from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base 
from dataclasses import dataclass

Base = declarative_base()

@dataclass
class AbstractModel(Base):
    __abstract__ = True

    name: str = Column(String, default=None) #None optional
    surname: str = Column(String, default=None)
    age: int = Column(Integer, default=None)
    city: str = Column(String, default=None)

@dataclass
class Model(AbstractModel):  #ERROR if AbstractModel is not inherited!!!
    __tablename__ = 'people'
    id: int = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self, name=None, surname=None, age=None, city=None):
        super().__init__(name=name, surname=surname, age=age, city=city)
        
@dataclass
class Model2(AbstractModel): #ERROR if AbstractModel is not inherited!!!
    __tablename__ = 'people2'
    id: int = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self, name=None, surname=None, age=None, city=None):
        super().__init__(name=name, surname=surname, age=age, city=city)


   
