class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def set_average_score(self, new_score):
        self.average_score = new_score

jane_doe = Student(name='Jane', surname='Doe', age=26, average_score=0)
print(jane_doe.average_score)

jane_doe.set_average_score(100)
print(jane_doe.average_score)

