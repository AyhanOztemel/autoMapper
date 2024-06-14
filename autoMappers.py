
from models import AbstractModel
from modeldto import AbstractSourceDto
from sqlalchemy.orm import class_mapper
from sqlalchemy.orm.state import InstanceState
import json
import typeguard
from typing import Type, Union
class AutoMapper():
    
    @typeguard.typechecked
    @staticmethod
    def autoMapperMethod(instance:Union[AbstractSourceDto,AbstractModel]=None,SourceClass:Union[Type[AbstractSourceDto],Type[AbstractModel]]=None):
                                                          
        if hasattr(instance, '_sa_instance_state') and isinstance(instance._sa_instance_state, InstanceState):
            print(f"This {type(instance).__name__}'instance belongs to a Model- SQLAlchemy ORM class.")
            
            def to_dict(instance):
                sourceInstance=SourceClass()
                
                #instance property list
                instancePropertyList=list(sourceInstance.__dict__.keys())
                
                # Get columns from  model
                columns = [column.key for column in class_mapper(instance.__class__).columns]           
                return {column: getattr(instance, column) for column in columns if column in instancePropertyList}
           
            obj_dict = to_dict(instance)  #Converts instance to dictionary 
            json_data = json.dumps(obj_dict, ensure_ascii=False)  #converts dictionary to json

            return json.loads(json_data,object_hook=lambda i: SourceClass(**i))

        else:
            print(f"This {type(instance).__name__}'instance does not belong to a Model-SQLAlchemy ORM class.")
            #Assigning SourceDto properties to a dictionary
            instanceDict = instance.__dict__
            json_data2 = json.dumps(instanceDict, ensure_ascii=False)
            return json.loads(json_data2,object_hook=lambda i: SourceClass(**i))
            
       


