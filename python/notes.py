class Person:
    def __init__(self,name):
        self.name = name

    def printinfo(self):
        print(f'Person name is {self.name}')

class Teacher(Person):
    def __init__(self,name,dept):
        super().__init__(name)
        self.dept = dept

    def printinfo(self):
        print(f'Person name is {self.name} from child class')

    def printdeptinfo(self):
        print(f'{self.name} is teaching in {self.dept}')


jami = Teacher('jami','cse')

jami.printdeptinfo()
jami.printinfo()