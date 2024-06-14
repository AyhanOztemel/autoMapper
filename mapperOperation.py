from models import Model,Model2,Base
from modeldto import SourceDto,Dto2
from autoMappers import AutoMapper
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


print("________________________________________")
def databaseAdd(model, name):
   
    # SQLAlchemy related codes
    #When memory database is used, id is reset in every session.Id is always one
    #If Test.db is used instead of memory the Id is automatically incremented
    engine = create_engine('sqlite:///:memory:') 
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Adding to database
    session.add(model)
    session.commit()
    Model=model.__class__ #convert instance to class
    # Example return query
    query = session.query(Model).filter_by(name=name).first()

    print("query----->", query)
    return query

model_1=databaseAdd(Model(name='John', surname='Doe', age=30, city='New York'),"John")  
print("TEST 1111111111111111111111111111111111111")
print("--------------converting from model to SourceDto-----------")
sourceDto=AutoMapper.autoMapperMethod(model_1,SourceDto)
print("model.name--->",model_1.name)
print("model.age--->",model_1.age)
print("model.city--->",model_1.city)
print("model.surname--->",model_1.surname)
print("model.id--->",model_1.id)
print("************************************************")
print("sourceDto.name--->",sourceDto.name)
print("sourceDto.age--->",sourceDto.age)
print("sourceDto.city--->",sourceDto.city)
try:
    print("sourceDto.id--->",sourceDto.id)
except Exception as e:
    print("Error-->",e)
print("________________________________________")

print("TEST 222222222222222222222222222222222222")
model_2= databaseAdd(Model2(name='Ayhan', surname='Oztemel', age=45, city='İstanbul'),'Ayhan') 
print("----------converting from model to Dto2--------------")

dto=AutoMapper.autoMapperMethod(model_2,Dto2)
print("model1.name--->",model_2.name)
print("model1.age--->",model_2.age)
print("model1.city--->",model_2.city)
print("model1.surname--->",model_2.surname) 
print("model1.id--->",model_2.id)
print("*************************************************")
print("dto.name--->",dto.name)
print("dto.age--->",dto.age)
print("dto.city--->",dto.city)
try:
    print("sourceDto.id--->",dto.id)
except Exception as e:
    print("Error-->",e)
print("________________________________________")

print("TEST 3333333333333333333333333333333333333333333")
print("-----------converting from SourceDtol to model-----------")
sourceDto=SourceDto(name="İlknur",age=42,city="Trabzon")
model_4=AutoMapper.autoMapperMethod(sourceDto,Model)
print("model_4---------->",model_4)
model_5=databaseAdd(model_4,"İlknur")

print("model.name--->",model_5.name)
print("model.age--->",model_5.age)
print("model.city--->",model_5.city)
print("model.surname--->",model_5.surname)#Dto2 dont have surname so surname's value is None
print("model.id--->",model_5.id) #from database ---> autoincrement

print("__________________________________________")
print("TEST 4444444444444444444444444444444444444444444444444")
print("----------------converting from Dto2 to model--------------")
dto2=Dto2(name="Mustafa",age=43,city="Rize")
#model_6=AutoMapper.autoMapperMethod(dto2,Model)
#print("model_6----->",model_6)
model_7=databaseAdd(AutoMapper.autoMapperMethod(dto2,Model2),"Mustafa")
print("model2.name--->",model_7.name)
print("model2.age--->",model_7.age)
print("model2.city--->",model_7.city)
print("model2.surname--->",model_7.surname)#Dto2 dont have surname so surname's value is None
print("model2.id--->",model_7.id)  #from database---> autoincrement
print("__________________________________________")


