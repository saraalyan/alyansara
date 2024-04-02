from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self):
        pass
    def characteristic(self):
        pass

    def actions(self):
        pass

class Employee(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def characteristic(self):
        return "sllll"

    def actions(self):
        return ["xz", "df"]


emp = Employee("saara")

print("Employee Name:", emp.name)
print("Employee Characteristic:", emp.characteristic())
print("Employee Actions:", emp.actions())
