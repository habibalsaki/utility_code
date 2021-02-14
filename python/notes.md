## Python

### lambda function

```python
divide = lambda x,y : x / y

print(divide(15,5))
```

### Creating Class
```python
class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Habib',[87,98,79])

# printing which class this object is representing
print(student_one.__class__)

print(student_one.average())

print(Student.average(student_one))
```

- some dunder methods
```python
class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)

    def __getitem__(self,i):
        return self.cars[i]

    def __repr__(self):
        return f'<Garage {self.cars}'

    def __str__(self):
        return f'Garage has {len(self)} cars'

toyota = Garage()
toyota.cars.append("Alion")
toyota.cars.append("Premio")

print(len(toyota))
print(toyota[0])
print(toyota)

```

### Inheritance
```python
class Person:
    def __init__(self,name):
        self.name = name

    def printinfo(self):
        print(f'Person name is {self.name}')

class Teacher(Person):
    def __init__(self,name,dept):
        super().__init__(name)
        self.dept = dept

    def printdeptinfo(self):
        print(f'{self.name} is teaching in {self.dept}')


jami = Teacher('jami','cse')

jami.printdeptinfo()
jami.printinfo()
```

### @property decorator
> if you want to covert a method to property, add @property decorator above the method

### @classmethod and @staticmethod
> both are used to define class methods, first one has the reference of class, where second one lacks it.

