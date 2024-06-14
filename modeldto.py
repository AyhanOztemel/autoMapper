import typeguard
from abc import ABC, abstractmethod


class AbstractSourceDto(ABC):
    @abstractmethod
    def __init__(self, name=None, age=None, city=None):pass


#!!!!!!!!!!!!!!!!!! None is a must !!!!!!!!!!!!!!!!!!!!!!
class SourceDto(AbstractSourceDto):#ERROR if AbstractSourceDto is not inherited!!!
    @typeguard.typechecked
    def __init__(self, name:str=None, age:int=None, city:str=None):
        self.name = name
        self.age = age
        self.city = city
#!!!!!!!!!!!!!!!!!! None is a must !!!!!!!!!!!!!!!!!!!!!!
class Dto2(AbstractSourceDto):#ERROR if AbstractSourceDto is not inherited!!!
    @typeguard.typechecked
    def __init__(self, name:str=None, age:int=None, city:str=None):
        self.name = name
        self.age = age
        self.city = city
