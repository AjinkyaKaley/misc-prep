from typing import List
import json
class Test:
    def __init__(self):
        self.data = []
        with open('jsonInput.json', 'r') as f:
            self.data = json.load(f)
            print(self.data)


class Student(object):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class Team(object):
    def __init__(self, students):
        self.students = students

    @classmethod
    def from_json(cls, students):
        students = list(map(Student.from_json, students))
        return cls(students)

student1 = Student(first_name="Jake", last_name="Foo")
student2 = Student(first_name="Jason", last_name="Bar")
team = Team(students=[student1, student2])
# Serializing
data = json.dumps(team, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# print(data)
i = json.loads(data)
# Deserializing
# decoded_team = Team.from_json(**i)
# This gives stundent as dict and not student object
decoded_team = Team(**json.loads(data))

# print(decoded_team)
# print(type(decoded_team.students[0]))
# print(decoded_team.students)

json_data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
serailize = json.dumps(json_data, indent=2, sort_keys=True)
# print(serailize)
deserialize = json.loads(serailize)
# print(deserialize)
sln = Test()
# # print(sln.data)
# d = json.loads(json_data)
# print(d['a'])
