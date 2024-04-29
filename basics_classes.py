# class Car:
#     def __init__(self,a,b) -> None:
#         self.a = a
#         self.b = b

#     # method
#     def tire(self):
#         return self.a
    
#     def tire2(self):
#         self.b

# # OOP's -> Object Oriented Programmings
# bmw = Car("MRF","CEAT")
# toyota = Car("XYZ","ABC")

# print(bmw.a)
# print(toyota.a)

# # def test(b:float,c:float) -> float:
# #     return b+c



# # a = test(1,3)#arguments
# # print(a)
 
# # test(1,2)

# #test()

# # Inheritance: class A inherits class B's props
# # Parent class
# class Person:
#     def __init__(self, fname, lname) -> None:
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         return self.firstname, self.lastname

# # a = Person("suman", "banik")
# # a.printname()

# # Child class   

# # class Student(Person):
# #     def __init__(self, grade, rollno, fname, lname) -> None:
# #         # Person.__init__(fname, lname)
# #         super().__init__(fname, lname)
# #         self.grade = "A"
# #         self.rollno = 10
        

# # x = Student("A", 100, "abc", "xyz")
# # abc = set(x)

# # x.printname()


# # Iterators
# # Iterable and Iterators.
# # List, tuples, disctionaries, sets are all iterable containers.

# a = ("Apple", "Banana", "Cherry")
# b = "Apple"
# c = list(a)
# d = {"x": 1, "y": 2, "z": 3, "s": 4}

# # for i in a: # a/b/c/d
# #     print(a) # it will itterate because of the iterable function hidden in it.

# # z = iter("sun")
# # print(next(z))
# # print(next(z))
# # print(next(z))

# class Numbers:
#     def __iter__(self) -> int:
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#     def __str__(self) -> str:
#         return "This is a iter class!!!"

# g = Numbers()

# h = iter(g)

# print(h)


# # print(next(h))
# # print(next(h))
# # print(next(h))
# # print(next(h))
# # print(next(h))


# # Polymorphism
# # len("Banana")
# # len([1,2,3,4,5])
# # len({'a':1,'b':2})



class Vehicle:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!!!")

class Car(Vehicle):
    def __init__(self, brand, model, speed) -> None:
        super().__init__(brand, model)
        self.speed = speed
    pass


class Boat(Car):
    def move(self):
        print("Sail!!!")


class Plane(Vehicle):
    def move(self):
        print("Fly!!!")



car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()