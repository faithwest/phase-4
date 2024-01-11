from sqlalachemy.orm import declarative_base, validates
from sqlalachemy import Column,BigInteger,Integer,String,DateTime,Boolean,Enum
from datetime import datetime
from sqlalachemy import engine

Base=declarative_base()

db_url=

engine=create_engine(db_url)

Class GenderEnum(Enum)#whatever you have in this class will work as a string
    male='male'
    female='female'
    other='other'



class Students (Base):
__tablename__="Student"

id = Column(Integer, primary_key=True)
name=column(String(50),nullable=False)
email=Column(String(250),nullable=False)
phone=Column(String(50),nullable=False)
is_married=Column(Boolean(50),nullable=False default=False)--edit false
gender=Column(String(50),nullable=True)

@validates('name ')
def validate_name(self, key, name):   --this is for checking if the name is
    if len(name) ≤ 4:
        raise ValueError("Name must be at least 4 characters long")
    return name

@validates(' email ')
def validate_name(self, key, email):   --this is for checking if the name is
    if len(email) ≤ 4:
        raise ValueError("Name must be at least 4 characters long")
    return email

@validates(' gender ')
def validate_gender(self, key, genders):   --this is for checking if the name is
    genders=['male','female','others']
    if gender in genders:
        return gender
    else:
        raise vallueError('Gender is not valid')


'''using PYTHON
new_user=Student(name=.'page', email='page@gmail.com',phone='44890493490',is_married=True,gender='male')

session.add(new_user)
session.commit()

using SQL

1. class method
@class method
def get_male_students(cls,session):
    return session.query(cls).filter(cls.gender==='male).all()
then>>
male_students=Students.get_male_students(session)
for student in male_students:
    print(student.name,'',student.email)
session.close()    
'''
