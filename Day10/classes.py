import operator

print(dir(operator))


# CLASS, OBJECTS, METHODS, ATTRIBUTES, OPERATOR OVERLOADING

class Person:
    count=0
    def __init__(self):
        Person.count=Person.count+1
p1=Person()
p2=Person()
p3=Person()
# 1+2=3
# '1'+'2'='12'
# THE COMMENTED CODE BELOW IS FOR ONE WITHOUT CONSTRUCTOR THAT WAS SHOWN IN CLASS

# p1 = Person()
# print(type(p1))
p1.describe()

# p1.name = 'John'
# p1.age = 18

# p1.describe()
p1 = Person('John', 18)

print(type(p1))
p1.describe()
p1.speak('Hello')

print(p1.name)
print(p1.age)

p2 = Person('Testing', 20)
p2.describe()

p1.name = 'Apple'
p1.age = 20

print(p1.name)
print(p1.age)

print(Person.__doc__)


# After operator overloading
print(p1+p2)
print(p2-p1)


# INHERITANCE
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def describe(self):
        print(f'My name is {self.name}')    

class Student(Person):
    def __init__(self, name, age, level):
        super().__init__(name, age)
        self.level = level

    def describe(self):
        super().describe()
        print(f'{self.name} is {self.age} years old and is in {self.level}')


class Worker(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def describe(self):
        super().describe()
        print(f'{self.name} is {self.age} years old and earns {self.salary}')


class Teacher(Worker):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age, salary)
        self.subject = subject

    def describe(self):
        super().describe()
        print(
            f'{self.name} is {self.age} years old and earns {self.salary} and teaches {self.subject}')

s1 = Student('John', 10, 6)
# s1.speak('Testing')
s1.describe()

w1 = Worker('Testing', 30, 20000)
w1.describe()

t1 = Teacher('ram', 40, 30000, 'CS')
t2 = Teacher('shyam', 20, 40000, 'msth')

t1.describe()


    # def __gt__(self, other):
    #     return self.salary > other.salary

    # def __ge__(self, other):
    #     return self.salary >= other.salary

    # def __eq__(self, other):
    #     return self.salary == other.salary

    # def __lt__(self, other):
    #     return self.salary < other.salary

    # def __le__(self, other):
    #     return self.salary <= other.salary



print(t1 < t2)
print(t1 <= t2)
print(t1 == t2)
print(t1 >= t2)
print(t1 > t2)


# Person -> Worker -> Teacher


# Creating a custom complex class
#a+ib
# z1=1+2i
# z2=2+3i
# z1+z2=3+5i
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def abs_value(self):
        return (self.real**2 + self.imag**2)**0.5

    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5

    def __add__(self, other):
        return Complex(self.real+other.real, self.imag+other.imag)

    def __sub__(self, other):
        return Complex(self.real+other.real, self.imag+other.imag)

    def __str__(self):
        return '{}+{}i'.format(self.real, self.imag)


c1 = Complex(1, 2)
c2 = Complex(2, 3)
print(abs(c1))


print(c1)
c3 = c1+c2
print(type(c3))
print(c3)


