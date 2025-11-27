# import first as f
# print(first.a)
# print(first.add(first.a,first.b))

# print(f.a)

# import first

# print(first.a)
# print(first.b)

# from first import add

# a=1
# b=2

# print(add(a,b))
# print(first.sub(a,b))

# function inside a function

# def outer():
#     def inner():
#         print('inner')
#     return inner

# calling function inside another function

# def hello():
#     print('hello')

# def my_fun(fun):
#     fun()

# my_fun(hello)

# decorator

# def outer_fun(fun):
#     def inner_fun(p,q):
#         print('pahele')
#         res=fun(p,q)
#         print(res)
#         print('baad')
#         return res
#     return inner_fun

# @outer_fun
# def add(p,q):
#     return p+q

# add(1,2)

# modifying data with dacorator

# def outer_fun(fun):
#     def inner_fun(p,q):
#         p=p+10
#         q=q+10
#         res=fun(p,q)
#         return res
#     return inner_fun

# @outer_fun
# def add(p,q):
#     return p+q

# print(add(1,2))

# adding before and after function call

# def outer_fun(fun):
#     def inner_join(message):
#         print('pahele')
#         fun(message)
#         print('baad')
#         return None
#     return inner_join


# @outer_fun
# def show(message):
#     print(message)

# show('hey')

# making class

# class MyClass:
#     '''this is my class'''

# Magic methods in class

# print(dir(MyClass))
# print(dir())
# print(__name__)

# print(MyClass.__doc__)
# print(MyClass.__dict__)
# print(MyClass.__module__)

# print(id(MyClass))
# obj1=MyClass
# obj2=MyClass
# obj3=MyClass
# print(id(obj1),id(obj2),id(obj3))

# class Students:
#     '''student data'''
#     def __init__(self):
#         print('external constructor call')
#         print(id(self))

# print(id(Students))
# obj1=Students()
# obj2=Students()
# print(id(obj1),id(obj2))
   
# class student:
#     '''details for students'''
#     def __init__(self):
#         print("external constructor")
#         print(id(self))
    
# obj1=student()
# print(id(obj1))

# class student:
#     def __init__(self):
#         print("external constructor")

# obj=student()
# obj.__init__()

# class student:
#     def __init__(self):
#         print("external constructor 1")

#     def __init__(self):
#         print('external constructor 2')
    
#     def __init__(self):
#         print("external constructor 3")
    
# obj=student()

# class student:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
# obj1=student('yash',21)
# print(obj1.n)
# print(obj1.a)
# obj2=student('raj',22)
# print(obj2.n)
# print(obj2.a)

# def new():
#     global x
#     x=10
#     print(x)
# new()
# print(x)

# class student:
#     school='shss'
#     def __init__(self,name):
#         self.n=name
#         print(self.n)
         
#     def addnew(self,contact):
#         self.c=contact
#         print(self.n,self.c,self.school_code)    
 
# obj=student('yash')
# obj.school_code=101
# obj.addnew(12345)
# print(obj.n,obj.c,obj.school_code)

# instance method

# class student:
#     def __init__(self,name,clas):
#         self.n=name
#         self.c=clas
#     def display(self):
#         print(f'{self.n} is name and {self.c} is class')
        
# obj=student('yash','BCA')
# obj.display()

# class student:
#     def __init__(self,balance):
#         self.balance=balance
    
#     def deposit(self,amount):
#         self.balance=self.balance+amount

#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance=self.balance-amount
#             return True
#         return False

# class method ka example

# class car:
#     wheels=4
    
#     @classmethod
#     def change_wheels(cls,count):
#         cls.wheels=count

# print(car.wheels)
# car.change_wheels(6)
# print(car.wheels)

# staticmethod

# class student:
#     def __init__(self):
#         pass

#     @staticmethod
#     def add(x,y):
#         return x+y
    
# s=student()
# print(s.add(10,20))

# checking if a marks is valid with staticmethod

# class student:
#     @staticmethod
#     def check(marks):
#         return 0<=marks<=100
    
# print(student.check(88))
# s=student()
# print(s.check(101))   




