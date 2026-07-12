class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        self.name = name
        self.salary = salary
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

alex = TeamLead("Alex", 1000, "Development", "Python", 5)

print(alex.name)
print(alex.salary)
print(alex.department)
print(alex.programming_language)
print(alex.team_size)