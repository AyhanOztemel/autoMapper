import typeguard
from abc import ABC, abstractmethod


class AbstractSourceDto(ABC):
    @abstractmethod
    def __init__(self, name=None, age=None, city=None):pass


#!!!!!!!"| None = None" used necessary !!!!!!!!!!!!!!!!!!!!!!

class SourceDto(AbstractSourceDto):#ERROR if AbstractSourceDto is not inherited!!!
    @typeguard.typechecked  
    def __init__(self, name:str| None = None, age:int| None = None, city:str| None = None):
        self.name = name
        self.age = age
        self.city = city


#!!!!!!!"| None = None" used necessary !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Dto2(AbstractSourceDto):#ERROR if AbstractSourceDto is not inherited!!!
    @typeguard.typechecked
    def __init__(self, name:str| None = None, age:int| None = None, city:str| None = None):
        self.name = name
        self.age = age
        self.city = city
