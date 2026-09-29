class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(self.name, "is doing regular work.")

    def describe(self):
        print(self.name, "- Salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary) # reuse parent
        self.team_size = team_size # add new data

    def work(self): # EXTEND
        super().work()
        print(self.name, "is also managing", self.team_size, "people.")

m = Manager("Ana", 80000, 5)
m.work()
m.describe()
print(isinstance(m, Employee))