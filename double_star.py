from pydantic import BaseModel
from typing import Literal

class Student(BaseModel):
    name:str
    roll_no:int
    age:int
    gender:Literal["Male", "Female"]

student1 = {'name': 'Abhishek', 'roll_no': 2, 'age': 23, 'gender':'Male'}

structure = Student(**student1)

print(structure)