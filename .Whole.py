# x=10
# y=20
# z=30
# print(x<y and y>z)
# print(bin(x))
# print(oct(x))
# x="34455"
# print(type(x))
# str='This is a Type'
# print(str.title())
# print(str.capitalize())
# print(str.swapcase())
# x=str.split()
# print(x)
# y=''.join(x)
# print(y)
# print(str.count("T"))

# l1=['this','is','a','list']
# l1.sort()
# l1.reverse()
# print(l1)
# l1.pop()
# print(l1)
# l1.remove('is')
# print(l1)
# # del l1
# # print(l1)
# l2=l1.copy()
# print(l2)
# print(id(l1))
# print(id(l2))
# import sys
# x=''
# y=[]
# z=()
# print(sys.getsizeof(x))
# print(sys.getsizeof(y))
# print(sys.getsizeof(z))


#   set 

# s1={'neeraj','raj',"rahul"}
# s2={10,20,30,40.5,50}
# print(max(s1))
# print(min(s2))
# print(min(s1))
# print(max(s2))
# print(len(s1),len(s2))
# print(type(s1),type(s2))
# print(id(s1),id(s2))
# print(sum(s2))
# s3=s1.copy()
# print(s3)
# print(s3)
# s1.clear()
# print(s1)

# l=["bharat","mata","ki","jai"]
# s1.add("bro")
# print(s1)

# s1.update(l)
# print(s1)

# s2.remove(50)
# print(s2)


# s2.remove(50)
# print(s2)

# s2.discard(50)
# print(s2)


# s2.discard(50)
# print(s2)

# s2.pop()
# print(s2)
# s2.pop()
# print(s2)

# ss={1,2,3,4,5,6}
# sss={3,6,7,8}
# print(ss.union(sss))
# print(ss)
# print(sss)

# print(ss.intersection(sss))
# print(ss)
# print(sss)

# print(ss.intersection_update(sss))
# print(ss)
# print(sss)

# print(ss.difference(sss))
# print(ss)
# print(sss)

# sss.difference_update(ss)
# print(ss)
# print(sss)

# print(ss.symmetric_difference(sss))
# print(ss)
# print(sss)

# sss.symmetric_difference_update(ss)
# print(sss)
# print(ss)

# s1={10,20,"raj","neeraj",30,40,"rahul"}
# s2={10,20,30,40.5,50}
# print(s1)
# print(type(s1))

# print(max(s1),max(s2))
# print(min(s1),min(s2))
# print(len(s1),len(s2))

# s4=s1.copy()
# print(s4)
# print(type(s4))
# print(id(s1),id(s4))

# s1.clear()
# print(s1)

# l=["dhoni",'sachin','raina']
# s1.update("bro","bore")
# s1.update(l)
# print(s1)

# t=("dhoni",'sachin','raina')
# s1.add(l)
# print(s1)

# print(s1.pop())
# print(s1)

# s1.remove("neeraj")
# print(s1)

# s1.remove("neeraj")
# print(s1)

# s1.discard("neeraj")
# print(s1)

# s1.discard("neeraj")
# print(s1)

# a={1,2,3,4,5,6}
# b={3,6,7,8}

# print(a.union(b))
# print(a.intersection(b))
# b.intersection_update(a)
# print(b)
# print(a.difference(b))
# a.difference_update(b)
# print(a)
# print(b.symmetric_difference(a))
# print(a.symmetric_difference(b))
# a.symmetric_difference_update(b)
# print(a)

# ss="string"
# x=frozenset(ss)
# print(x)
# print(type(x))

# A={2,4,6,8}
# B={1,3,5,7,6,8}

# x=frozenset(A)
# # print(x)
# y=frozenset(B)
# # print(y)

# t={1,2,3,4,5}
# u={2,5}

# print(x.union(y))
# print(x.intersection(y))
# print(x.difference(y))
# print(x.symmetric_difference(y))

# print(x.isdisjoint(y))
# print(t.issuperset(u))
# print(u.issubset(t))

    # Control statement  

# x=int(input("enter the number"))
# x=11
# if x%2==0:
#     print("even number")

# else:
#     print("odd number")

# x=int(input("enter the number 1"))
# y=int(input("enter the number 2"))
# x=10
# y=20
# if x>y:
#     print(f'{x} is greater')

# else:
#     print(f'{y} is greater')

#    if else practice in python -------------------------------------------------------------

# x=10
# if(x%2==0):
#     print("even number")

# else:
#     print("odd number")


# c1=36
# c2=34
# if(c1>c2):
#     print(f' c1 ({c1}) is greater than c2')

# else:
#     print(f' c2 ({c2}) is greater than c1')

x=10
y=20
z=30

# if(x>y):
#     if(x>z):
#         print("x is greater")
#     else:
#         print("z is greater")
# else:
#     if(y>z):
#         print("y is greater")
#     else:
#         print("z is greater")

# if(x>y and x>z):
#     print("x is greater")
# else:
#     if(y>x and y>z):
#         print("y is greater")
#     else:
#         print("z is greater")

#  --------- -------------- --------------- ------------ -------------

#    string datatype ---------------------------------

string="Python Is a Programming language"
# print(string)
# print(type(string))
# print(min(string))
# print(max(string))
# print(len(string))
# string2=input("enter any string")
# print(string.capitalize())
# print(string.find("P",1))
# print(string.find("z"))
# print(string.index("P"))
# print(string.index("z"))
# print(string.split("o",1))
# l1=['yash','boss','cricket']
# x=' '.join(l1)
# print(x)
# print(string.count("g"))
# l1=[10]
# l2=[10]
# print(id(l1),id(l2))

#   list datatype ---------------------------------------

# listt=[10,10.5,"neeraj"]
# print(listt)
# print(type(listt))
# listt.extend("this")
# print(listt)
# listt.extend([45,6,7,8,6])
# print(listt)
# listt.insert()
# listt.insert(2,"this")
# print(listt)
# listt.reverse()
# print(listt)
# list1=[10,20,40,30,10,100]
# list1.sort()
# print(list1)
# list1.reverse()
# print(list1)
# list1.pop()
# print(list1)
# list1.remove(10)
# print(list1)
# list1.clear()
# print(list1)
# list2=list1.copy()
# print(list1,list2)
# print(id(list1),id(list2))
# print(list1.count(100))
# print(list1.index(10))
  
# import sys

# x=''
# y=[]
# z=()

# print(sys.getsizeof(x))
# print(sys.getsizeof(y))
# print(sys.getsizeof(z))

#   tuple datatype ---------------------------------

# tuplee=(10,20,30,40,50,60)
# tuplee1=(10,20,30,40,50,60)
# print(tuplee)
# print(type(tuplee))
# print(id(tuplee),id(tuplee1))
# print(tuplee.index(40))
# print(tuplee.count(40))

#   Dictionary datatype -------------------------------

d={"name":"Neeraj","age":37,"quali":"M.tech"}
# print(max(d))
# print(min(d))
# print(len(d))
# print(type(d))
# print(id(d))
# d.clear()
# print(d)
# d1=d.copy()
# print(d1)
# print(id(d),id(d1))
# ll=["key1","key2","key3",45]
# d2=dict.fromkeys(ll)
# print(d2)
# print(d['name'])
# print(d.get("name"))
# print(d.keys())
# print(d.values())
# print(d.items())
# d.popitem()
# print(d)
# d.pop("name")
# print(d)
# d.setdefault("bro","yash")
# print(d)
# u={}
# u.update(d)
# print(u)

#   Set datetype ----------------------------------

# se={10,20,30,40,"raj","yash"}
# print(se)
# print(type(se))

s1={"neeraj","jatin","himanshu"}
s2={10,20,30,40.5,50}
# print(len(s2))

# s3=s1.copy()
# print(s3)
# print(id(s1),id(s3))
# s3.clear()
# print(s3)
# print(s2)
# s2.add(60)
# print(s2)
# l=[10,40,80]
# s2.update(l)
# print(s2)

# s2.pop()
# print(s2)
# s2.discard(10)
# print(s2)
# s2.discard(10)
# print(s2)

a={1,2,3,4,5,6}
b={3,6,7,8}
# print(a.union(b))
# print(a.intersection(b))
# print(b.intersection_update(a))
# print(b)
# print(a.difference(b))
# print(b.difference(a))
# print(b.difference_update(a))
# print(b)
# print(a.symmetric_difference(b))
# print(b.symmetric_difference_update(a))
# print(b)

#  frozneset datatype --------------------------------

# i=1
# while i<=10:
#     print(i,end=" ")
#     i=i+1

# i=1
# while i<=10:
#     x=2*i
#     print(f'2 * {i} = {x}')
#     i=i+1

# print("Hello",end=" ")
# print("world")


#   which number is greater with  ( if elif else )

# x=0
# y=-779
# z=0

# if (x>y and x>z):
#     print("x is greater")
# elif (y>x and y>z):
#     print("y is greater")
# elif (z>x and z>y):
#     print("z is greater")
# elif (x==y and y==z):
#     print("all the numbers are equal")
# elif(x==y):
#     print("x and y are equal")
# elif(y==z):
#     print("y and z are equal")
# elif(z==x):
#     print("x and z are equal")

# s="neeraj"
# l=[10,20,30,40]
# t=(1,2,3,7,4)
# d={"name":"neeraj","quali":"M.tech"}
# s1={"neeraj","rahul","jai"}

# x=frozenset(s)
# print(x)
# y=frozenset(s)
# print(y)
# print(id(x),id(y))
# ding=frozenset(l)
# print(ding)
# ting=frozenset(t)
# print(ting)
# parrot=frozenset(d)
# print(parrot)
# sing=frozenset(s1)
# print(sing)

# s1={1,2,3,4,5,6}
# s2={5,6,7,8}
# x=frozenset(s1)
# # print(x)
# y=frozenset(s2)
# print(y)
# print(s1.issuperset(s2))
# print(s2.issubset(s1))
# print(s1.isdisjoint(s2))
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))

#    To print nunbers in the same line with comma (,) -------------------------

                                 # 1,2,3,4,5,6,7,8,9,10

# i=1
# while (i<=10):
#     if(i<10):
#         print(i,end=",")
#     else:
#         print(i)

#     i=i+1

#    to count the digits in a number ---------------------
 
# n=123457
# hdigit=0

# while n>0:
#     hdigit=hdigit+1
#     n= n//10

# print(hdigit)
# print(n)

#    for practice ------------------------

# n=12345
# sum=0
# while (n>0):
#     yoo=n%10
#     sum=sum+yoo**2
#     n=n//10
# print(sum)
# print(n)

    # Armstrong check --------------------------------

# n=12345
# x=y=n
# count=0
# while (n>0):
#     count=count+1
#     n=n//10

# sum=0
# while (x>0):
#     yoo=x%10
#     sum=sum+yoo**count
#     x=x//10

# if (y==sum):
#     print("the given number is palindrome")
# else:
#     print("the given number is not a palindrome number")

#  Palindrome Check ---------------------------

# rv=0
# n=121
# x=n
# while (n>0):
#     a=n%10
#     rv=rv*10+a
#     n=n//10
# if(rv==x):
#     print("the number is palindrome")
# else:
#     print("the number is not palindrome")

#   for loop --------------------------

# n=input("enter the input")
# for i in n:
#     print(i)

# n=input("enter the string")

# for i in n:
#     x=ord(i)+4
#     y=chr(x)
#     print(y,end="")

# n=input("enter the string")
# # n="madam"
# if(n==n[::-1]):
#     print("the string is palindrome")
# else:
#     print("not")

# for i in range(5):
#     print(i)
# print("done!")

# for i in range(1,6):
#     print(i)
# print("done!")

# for i in range(1,10,2):
#     print(i)
# print("done!")

# x=range(1,11)
# print(list(x))
# print(tuple(x))
# print(dict(x))

# x=range(-1,-11,-1)
# print(list(x))

# x=range(-10,0)
# print(list(x))

# x=range(-1,-11)
# print(list(x))

#  n even with range -----------------

# n=int(input("enter the number"))
# x=range(2,n+1,2)
# print(list(x))

#   n odd with range ----------------

# n=int(input("enter the number"))
# x=range(1,n+1,2)
# print(list(x))

# n=input("enter the string")
# es=""
# l=len(n)
# for i in range(l-1,-1,-1):
#     es=es+n[i]
# print(es)

# if(es==n):
#     print("palindrome")
# else:
#     print("not")

