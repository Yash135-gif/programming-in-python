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

# question 1

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show_details(self):
#         print(f'Name: {self.name} Age: {self.age}')

# p1=person('yash',21)
# p1.show_details()

# question 2

# import math

# class circle:
#     def __init__(self,radius):
#         self.radius=radius
    
#     def area(self):
#         return math.pi*self.radius*self.radius
    
#     def circumference(self):
#         return 2*math.pi*self.radius

# c=circle(4)
# print("Area: ",round(c.area(),2))
# print("circumference: ",round(c.circumference(),2))
    
# question 3

# class student:
#     school_name='SJPCS'

#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll

#     def show(self):
#         print(self.name,self.roll,student.school_name)

# c1=student('yash',101)
# c2=student('yash2',102)

# c1.show()
# c2.show()
       
# question 4

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print(f"deposited = {amount} successfully, New balance = {self.balance}")

#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance=self.balance-amount
#             print(f'your withdrawal of {amount} is successful, Remaining Balance = {self.balance}')
#         else:
#             print(f'the bank balance is not sufficient for withdrawal of your amount')
    
#     def check_balance(self):
#         print(f'current balance = {self.balance}')

# acc=BankAccount('yash',500)
# acc.withdraw(200)
# acc.deposit(400)
# acc.check_balance()

# question 5

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
    
#     def get_tax(self):
#         print(f'Employee = {self.name}, Tax = {self.salary*0.1}')

# e1=Employee('yash',50000)
# e1.get_tax()

# question 6

# class Animal:
#     def speak(self):
#         print('i am an animal')
# class Dog(Animal):
#     def speak(self):
#         print('woof')
# class Cat(Animal):
#     def speak(self):
#         print('meow')

# a=Animal()
# d=Dog()
# c=Cat()

# a.speak()
# d.speak()
# c.speak()

# class ShoppingCart:
#     def __init__(self):
#         self.items={}

#     def add_item(self,item,price):
#         self.items[item]=price
#         print(f'Added = {item} - {price}')
    
#     def remove_item(self,item):
#         if item in self.items:
#             del self.items[item]
#             print(f'Removed item = {item}')
#         else:
#             print(f'given item {item} not found in remove_item')
    
#     def get_total(self):
#         return sum(self.items.values())
    
# cart=ShoppingCart()
# cart.add_item('shoes',1200)
# cart.add_item('shirt',800)
# print('Total',cart.get_total())

# question 8

# class Library:
#     def __init__(self):
#         self.books=[]
    
#     def add_book(self,title):
#         self.books.append(title)
#         print(f'Added = {title}')

#     def remove_book(self,title):
#         if title in self.books:
#             self.books.remove(title)
#             print(f'book {title} removed')
#         else:
#             print(f'Given book {title} not found')
        

#     def display_books(self):
#         print(f'Books in library = {self.books}')

# lib=Library()
# lib.add_book('physics')
# lib.add_book('chemistry')
# lib.display_books()

# question 9

# class Math:
#     @staticmethod
#     def factorial(n):
#         result=1
#         for i in range(1,n+1):
#             result=result*i
#         return result
    
#     @classmethod
#     def square(cls,x):
#         return x*x

# print(Math.factorial(5))
# print(Math.square(2))

# m=Math()
# print(m.factorial(4))
# print(m.square(4))

# question 10

# class Teacher:
#     def teach(self):
#         print('Teaching..')

# class Student:
#     def study(self):
#         print('Studing..')

# class TeachingAssistant(Teacher,Student):
#     def assist(self):
#         print('Assisting Teacher and helping students.')

# ta=TeachingAssistant()
# ta.teach()
# ta.study()
# ta.assist()

 

