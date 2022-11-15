from human import Human
from marknote import MarkNote

class Student(Human):
    def __init__(self, name, marknote):
        self.name = name
        # self.age = age
        # self.sex = sex
        if isinstance(marknote, MarkNote):
            self.note = marknote
        else:
            self.note = MarkNote()

        # self.alive = alive

    def study(self):
        pass

    def change(self, marknote):
        if isinstance(marknote, MarkNote):
            self.note = marknote

    def add(self, mark):
        self.note.add(mark)

    # def __str__(self):
    #     return f"{self.name}: age = {self.age};" \
    #            f" sex = {self.sex};" \
    #            f" mark = {self.mark};" \
    #            f" alive = {self.alive}"


m1 = MarkNote()
s1 = Student("Alex", m1)
s2 = Student("Kate", m1)
s3 = Student("Peter", m1)