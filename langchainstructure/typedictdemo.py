from typing import TypedDict


class Person(TypedDict):
    name:str
    age:int


name_person : Person = {
    "name": "Alice",
    "age": 30
}
print(name_person)    