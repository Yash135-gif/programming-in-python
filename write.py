# dictionary  

# data={'name': 'yash','age':21,'quali':'BCA'}
# print(data)
# print(id(data),type(data))

# tuple  

# t=(1,2,3,4,'yash','neeraj',10.4,[1,2,3])
# print(t,id(t),type(t))

# Boolean 

# x=True
# y=False
# print(x)
# print(type(x))
# print(y)
# print(type(y))

# string data type

# string functions

# str1='python'
# print(str1)
# print(type(str1))
# store=input('enter any value')
# print(type(store))
# print(max(str1))
# print(min(str1))
# print(len(str1))

# string methods

# str1='I Love python'
# l=['i','love','python']
# print(str1.upper())
# print(str1.lower())
# print(str1.swapcase())
# print(str1.capitalize())
# print(str1.title())
# print(str1.find('p'))
# print(str1.index('p'))
# print(str1.find('z'))
# # print(str1.index('z'))
# print(str1.split('o'))
# print(" ".join(l))

# split and join method 

# s='i love python'
# l=['i','love','java']
# print(s.split())
# print(' '.join(l))


# function of lists 

# print(type(l),type(l1))
# print(id(l),id(l1))
# print(len(l),len(l1))

# methods of lists

# l.append('sanju')
# print(l)

# l2=[1,2,3,4]
# l.extend(l2)
# print(l)

# l.insert(0,'chai')
# print(l)

# l2=[1,2,3,4]
# l.insert(0,l2)
# print(l)

# l1.reverse()
# print(l1)

# l2=[1,2,3,4,5]
# l2.sort(reverse=True)
# print(l2)

# l.pop()
# print(l)

# l1.remove()

# del l
# print(l)

# l.clear()
# print(l)

# l=[1,2,3,4,'yash','neeraj',4]
# l1=[1,2,3,4,'yash','neeraj']

# l3=l.copy()
# print(l3)

# print(l.count(4))

# print(l.index(4,5))

# import sys

# s=''
# l=[]
# t=()

# print(sys.getsizeof(s))
# print(sys.getsizeof(l))
# print(sys.getsizeof(t))

# function in tuple

# print(t,t1)
# print(id(t),id(t1))
# print(type(t),type(t1))

# print(max(t))
# print(min(t))
# print(sum(t))
# print(len(t))

# methods in tuple

# t=(1,2,6,5,3,4,5)
# t1=(1,2,3,4,5)

# print(t.count(5))
# print(t.index(1))

dict={'name':'yash','age':21,'quali':'Mtech'}

# function in dictionary 

# print(max(dict))
# print(min(dict))
# print(len(dict))
# print(type(dict))
# print(id(dict))

# methods in dictionary

dict1={'name':'yash','age':21,'quali':'Mtech'}

# dict.clear()
# print(dict)

# dict1=dict.copy()
# print(dict1)

# l=['yash','adam','jaya']
# dict2=dict.fromkeys(l,'yoo')
# print(dict2)

# s='abc'
# dict2=dict.fromkeys(s,200)
# print(dict2)

# print(dict1['name'])
# dict1['name']='yooo'
# print(dict1['name'])

# print(dict1.get('name'))
# print(dict1.get('age'))

# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

# print(dict1.setdefault('new','value'))
# print(dict1)

# dicta={'name':'yash','age':20}
# dictb={'age':21,'class':'BCA'}
# dicta.update(dictb)
# print(dicta)

dict1={'name':'yash','age':21,'quali':'Mtech'}

# dict1.pop('age')
# print(dict1)

# dict1.popitem()
# print(dict1)

# def myfun(x,y):
#     z=x+y
#     return z

# p=int(input('enter a value'))
# q=int(input('enter a value'))

# print(myfun(p,q))

# def myfu(p,q):
#     print(p+q)
    
# p=int(input("enter a value:"))
# q=int(input("enter a value:"))

# result=myfu(p,q)
# print(result)
# print(result)
# print(result)

# def add():
#     pass

# print(id(add))
# print(add())

# def myfu(p,q,r):
#     print(p)
#     print(q)
#     print(r)
# p,q,r=1,2,3
# print(myfu(p,q,r))

# def fun(name='guest',age=None,course=None):
#     print(name)
#     print(age)
#     print(course)

# name='yash'
# age=21
# course='BCA'

# fun(name,age,course)

# def fun(*args):
#     print(args)
#     print(type(args))

# fun(1,2,3)
# fun(1)

# t=(1,)
# print(type(t))

# def fun(*args):
#     total=0
#     print(type(args))
#     print(args)
#     for i in args:
#         total=total+i
#     return total

# result=fun(1)
# print(result)

# n=int(input("enter how many values you want to add"))
# l=[]
# for _ in range(n):
#     value=float(input("enter value:"))
#     l.append(value)

# def add(*args):
#     sum=0
#     for i in args:
#         for j in i:
#             sum=sum+j
#     return sum

# print(add(l))

# def show(name,**kwargs):
#     print('Name :',name)
#     for key,value in kwargs.items():
#         print(f'{key}:{value}')

# show('yash',age=21,course='BCA',yoo='yooo')

s={1,2,3,4,'neeraj','python'}

# functions in set

# print(type(s))
# print(s)
# ss={1,2,3,4,5}
# print(max(ss))
# print(min(ss))
# print(sum(ss))
# print(len(ss))

# methods in set

# sss=s.copy()
# print(sss)

# sss.clear()
# print(sss)

# ss.add(6)
# print(ss)

# ss.update([7,8,9,10])
# print(ss)

# ss={12,3,4,4,5,6,7}

# print(ss.pop())
# print(ss)

# ss.discard(12)
# print(ss)

# ss.discard(12)
# print(ss)

a={1,2,3,4,5,6}
b={3,6,7,8}

# print(a.union(b))
# print(a,b)

# print(a.intersection(b))
# print(b.intersection_update(a))
# print(a,b)

# print(b.difference(a))
# print(b.difference_update(a))
# print(a,b)

# print(a.symmetric_difference(b))
# print(a.symmetric_difference_update(b))
# print(a,b)
# print(b.symmetric_difference_update(a))
# print(a,b)

# a={1,2,3,4,5,6,7,8}
# b={7,8,4}

# print(a.isdisjoint(b))
# print(a.issuperset(b))
# print(b.issubset(a))

# n=int(input('enter a value'))
# if n%2==0:
#     print('even')
# else:
#     print('odd')

# while loop

# n=int(input("enter a number: "))
# i=1
# while i<=n:
#     print(i)
#     i=i+1

# with ,

# n=int(input('enter a number: '))
# i=1
# while i<=n:
#     if i<n:
#         print(i,end=',')

#     else:
#         print(i)

#     i=i+1

# n even numbers

# n=int(input("enter a number: "))
# i=1
# while i<=n:
#     if i<n:
#         print(2*i,end=',')
#     else:
#         print(2*i)
#     i=i+1

# Table

# n=int(input('enter a number: '))
# i=1
# while i<=10:
#     print(f'{n} * {i} = {n*i}')
#     i=i+1

# armstrong

# n=int(input('enter: '))
# x=y=n
# sum=0
# digit=0
# while n>0:
#     digit=digit+1
#     n=n//10

# while x>0:
#     last_digit=x%10
#     sum=sum+last_digit**digit
#     x=x//10

# if y==sum:
#     print('armstrong')
# else:
#     print('not')

# armstrong

# n=int(input('enter a number: '))
# x=y=n
# digit=0
# sum=0
# while x>0:
#     digit=digit+1
#     x=x//10
# while y>0:
#     last_digit=y%10
#     sum=sum+last_digit**digit
#     y=y//10
# if sum==n:
#     print('armstrong')
# else:
#     print('not')

# Finding average

# def find_average(lst):
#     if not lst:
#         return 'please enter list with some data'
#     total=sum(lst)
#     average=total/len(lst)
#     return average

# l=[1,2]
# print(find_average(l))

# Finding average 

# def find_average(lst):
#     if not lst:
#         return 'please enter list with some data'
#     sum=0
#     for num in lst:
#         sum=sum+num
#     average=sum/len(lst)
#     return average

# l=[5,4]
# print(find_average(l))

# calculator

# def calculator(a,b,cal):
#     if cal=='add':
#         return a+b
#     elif cal=='sub':
#         return a-b
#     elif cal=='multiply':
#         return a*b
#     elif cal=='divide':
#         return a/b
#     else:
#         return 'enter valid cal'
# print(calculator(2,8,'add'))

# To-Do List

# todo=[]
# while True:
#    print(' 1. Add Task \n 2. view Tasks \n 3. Exit')
#    choice=input('enter what you want to do:')

#    if choice=='1':
#       task=input('enter task: ')
#       todo.append(task)

#    elif choice=='2':
#       print('\n Your Tasks ')
#       for i,t in enumerate(todo,1):
#          print(f'{i}. {t}')

#    elif choice=='3':
#       break
   
#    else:
#       print('Invalid Choice')

# map higher order function

# numbers=[1,2,3,4]

# def square(num):
#     return num*num

# var=list(map(square,numbers))
# print(var)

# adding two different lists with map function

# l=[1,2,3,4]
# ll=[1,2]

# def ad(x,y):
#     return x+y

# var=list(map(ad,l,ll))
# print(var)

# sabsa chota iterables tak chalega

# l=[1,2,3,4,5]
# ll=[1,2,3,4,5]
# lll=[1,2]

# def ad(x,y,z):
#     return x+y+z

# res=list(map(ad,l,ll,lll))
# print(res)

# filter higher order function ka use

# l=[1,2,3,4,5]

# def greater_than_3(num):
#     return num>3

# res=list(filter(greater_than_3,l))
# print(res)

# from functools import reduce

# Max-digit with reduce

# l=[1,3,5,3,3]

# def max_digit(x,y):
#     if x>y:
#         return x
#     else:
#         return y
    
# print(reduce(max_digit,l))

# Adding string

# l=['python','is','fun']

# def show(a,b):
#     return a+' '+b

# res=reduce(show,l)
# print(res)

# lambda function

# add with lambda

# add=lambda x,y: x+y
# print(add(2,3))

# finding square with lambda

# square=lambda x: x*x
# print(square(5))

# filter with lambda

# l=[1,2,3,4,5,6]
# res=list(filter(lambda x: x%2==0,l))
# print(res)

# reduce with lambda

# l=[1,3,5,3,6,6]
# res=reduce(lambda x,y: x if x>y else y,l)
# print(res)

# res=list(filter(lambda x: x>2,l))
# print(res)

# putting n numbers in a list

# def new(n):
#     l=[]
#     for i in range(1,n+1):
#         l.append(i)
#     return l

# print(new(10))

# def my_generator(n):
#     for i in range(n):
#         yield i

# res=my_generator(10)
# print(next(res))
# print('hello')
# print(next(res))
# print('hii')
# print(next(res))
# print(next(res))

# checking what floor does

# x=123
# # x=x/10
# x=x//10
# print(x)

# checking if a number is palindrome with while loop

# n=int(input('enter a number: '))
# x=n
# rev_num=0
# while x>0:
#     rev_num=rev_num*10+x%10
#     x=x//10

# if n==rev_num:
#     print("palindrome")
# else:
#     print('not')

# for loop

# n=input('enter your name')
# for i in n:
#     print(i)

# changing alphabets

# n=input('enter a string: ')
# for i in n:
#     x=ord(i)+5
#     y=chr(x)
#     print(y,end='')

# printing string in reverse

# s='string'
# print(s[::-1])

# checking if a string is palindrome

# n=input('enter a string: ')
# if n==n[::-1]:
#     print('palindrome')
# else:
#     print('not')

# range

# x=range(1,11)
# print(list(x))
# print(tuple(x))

# trying range by putting wrong values

# x=range(-1,-11,1)
# print(x)
# print(list(x))

# concatination of string

# s1='yash'
# s2='gupta'
# print(s1+ " "+s2)

# reversing the string

# n='python'
# l=len(n)
# x=''
# for i in range(l-1,-1,-1):
#     x=x+n[i]

# print(x)

# checking palindrome with for loop

# n=input('enter any string:')
# l=len(n)
# x=''
# for i in range(l-1,-1,-1):
#     x=x+n[i]
# if x==n:
#     print('palindrome')
# else:
#     print('not')

# s='yash'
# print(s*5)

# n=4
# i=1
# while i<=4:
#     print('*'*i)
#     i=i+1

# checking global and local variable

# x=10
# def myfun():
#     global y
#     y=20
#     pass

# myfun()
# print(y)

# using global() function

# x=10
# def show():
#     print(globals()['x'])
#     x=20
#     print(x)

# show()
# print(x)

# factorial

# def fact(num):
#     result=1
#     while num>=1:
#         result=result*num
#         num=num-1
#     return result

# print(fact(5))

# def add_sub(a,b):
#     add=a+b
#     sub=a-b
#     return add,sub

# x,y=add_sub(100,50)
# print('The addition is: ',x)
# print('the subraction is: ',y)

# my_list=[10,20,30,40]
# def sqr(n):
#     return n*n

# x=map(sqr,my_list)
# print(x)
# print(list(x))

# my_str='Neeraj'
# def add(s):
#     ss=ord(s)
#     return ss

# result=list(map(add,my_str))
# print(result)

# def change(s):
#     x=ord(s)
#     return chr(x+5)

# result=list(map(change,my_str))
# print(result)

