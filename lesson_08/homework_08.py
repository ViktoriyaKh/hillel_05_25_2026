class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def set_average_score(self, new_score):
        self.average_score = new_score

Jane_Doe = Student(name='Jane', surname='Doe', age=26, average_score=0)
print(Jane_Doe.average_score)

Jane_Doe.set_average_score(100)
print(Jane_Doe.average_score)

