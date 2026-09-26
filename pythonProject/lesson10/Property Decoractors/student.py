
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


studenti1 = Student("Suela", 17)

print(studenti1.name)

print(studenti1.age)


studenti1.age = 255

print(studenti1.age)