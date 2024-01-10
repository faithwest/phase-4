from sqlalachemy.orm import declarative_base, validates
from sqlalachemy import Column,BigInteger,Integer,String,DateTime,Boolean,Enum
from datetime import datetime--comes with it
from sqlalachemy import engine
--engine import

Base=declarative_base()

db_url=

engine=create_engine(db_url)

Class GenderEnum(Enum)--whatever you have in this class will work as a string
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
############################################################################
'''
     POSTGRESS
pipenv install psycogy-binary(postgre)/pipenv install psycopg2

     ALEMBIC CONFIGURATIONS
alembic init migrations
ALEMBIC.INI corrections
edit the alembic.ini 
connection to database,(LQxqLTuAuT/29?#)
go to postgress instance:superbase:
copy url(database settings>>connection string)>>sql alchemy url and password line
delete table(ensure the supabase is empty:postgre instance is empty)

      ENVY.PY
import the models:knows which database to use(19)from model import base
target_metadata=base.metadata

       models
import sqlalachemy.orm import declarative_base
from sqlalachemy import BigInt,Interger,String,DataTime
from datetime import datetime(comes with it)
Base=declarative_base()
class Student(Base):
__tablename__="Student"

       run migrations
alembic revision --autogenerate -m 'Create student model' >>get a version/key/creates a table automatically
we wont see our students--if it makes sense then upgrade<upgrade head> 
alembic upgread heads>connect db, and create table students
alembic revision --autogenerate -m 'added gender'
alembic upgrade heads
python3 model.py>python
sqlquery>

    CONSTRAINTS
runs the validation
valid if you use the model ONLY but doeas not apply to database
can add them manually to the database

       ISSUES
deactivate all virtual environments

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

SQLLITE
installations= pipenv install sqlalchemy alembic
create table
'''
