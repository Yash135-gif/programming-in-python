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

# n=eval(input("enter the number"))
# i=1
# while(i<=n):
#     print(i)
#     i=i+1
# print("hello",end=" ")
# print("he")

  
# x=1
# i=1
# while(x<n):
#     x=2*i
#     print(x)
#     i=i+1
# print('hello')

# i=1
# while(i<=n):

#     if(i<n):{
#         print(i,end=",")
#     }
#     else:{
#         print(i)
#     }
#     i=i+1
 
# digit=0
# while(n>0):
#     digit=digit+1
#     n=n//10
# print(digit)
# print(n)
   

#    yoo -----------------------------------------------


# n=152
# x=n
# y=n
# digit=0
# while(n>0):
#     digit=digit+1
#     n=n//10
# print(digit)
# sum=0
# while(x>0):
#     ld=x%10
#     sum=sum+ld**digit
#     x=x//10
# if(y==sum):
#     print("the number is armstrong")

# else:{
#     print("no armstrong")
# }

# def add(x,y):
#     print("value of x = ",x)
#     print("value of y = ",y)
#     return x+y
# n=eval(input("enter the number"))
# m=eval(input("enter the number"))
# x=add(y=n,x=m)
# print(x)


# def add(x=2,y=2,z=2):
#     return x+y+z

# print(add(2,3,4))

# def sum(*n):
#   print(n)
#   print(type(n))
#   sum=0
#   for i in n:
#     sum=sum+i
#   return sum

# print(sum(2,3,4))

# def sum(*n):
#     sum=0
#     for i in n:
#         for x in i:
#             sum=sum+x
#     return sum
# p=eval(input("enter the tuple"))
# print(sum(p))

#   palindrome number ------------------------------------------------

# n=eval(input("enter the number"))
# rv=0
# c=n
# while(n>0):
#     rv=rv*10+n%10
#     n=n//10
# if(c==rv):
#     print("the given number is palindrome")

# else:
#     print("the given number is not a palindrome number")

#   Armstrong -------------------------

# count=0
# n=153
# x=n
# y=n
# while(n>0):
#     count=count+1
#     n=n//10
# sum=0
# while(x>0):
#     t=x%10
#     sum=sum+t**count
#     x=x//10

# if(y==sum):
#     print("the given number is armstrong")
# else:
#     print("not a armstrong number")

#   numbers horizontally ----------------------------------------
#  
# n=10
# i=1
# while(i<=10):
#     if(i<10):
#         print(i,end=",")
#     else:
#         print(i)
#     i=i+1


#    sum  of numbers ---------------------------------------------

# n=10
# i=1
# sum=0
# while(i<=10):
#     sum=sum+i
#     i=i+1
# print(sum)

#  even  

# n=20
# i=1
# while(i<=20):
#      if(i%2==0):
#         print(i)
#      else:
#           pass
#      i=i+1

#  even odd 

# n=19
# i=1
# # while(x<n-1):
# #     x=2*i
# #     print(x)
# #     i=i+1
# while(x<n):
#     x=2*i-1
#     print(x)
#     i=i+1


# n=20
# i=1
# while(i<=n):
#     if(i%2!=0):
#         print(i)
#     i=i+1

# a="abcd"
# for i in a:
#     x=ord(i)+4
#     y=chr(x)
#     print(y,end="")

# n="madam"
# if(n==n[::-1]):
#     print("palindrome")

# x=range(1,5)
# print(list(x))
# y=range(-10,5)
# print(tuple(y))

# n=20
# x=range(2,n+1,2)
# print(list(x))

# y=range(1,n+1,2)
# print(tuple(y))

# z=range(2,n+1,2)
# print(z)

# n="madsihotiam"
# x=''
# l=len(n)
# for i in range(l-1,-1,-1):
#     x=x+n[i]

# if(x==n):
#     print("palindrome")
# else:
#     print("not")

# n=10
# i=1
# while(i<=10):
#     if(i==6):
#         i=i+1
#         pass
#     print(i)
#     i=i+1

# n=eval(input("enter the value"))
# print(n)
# print(type(n))
# x="string"
# y=5*x
# print(y)

# n=5
# i=5
# while(i<=n):
#     print(' '*(n-i)+i*'* ')
#     i=i+1


# while(i>0):
#     print(' '*(n-i)+i*'* ')
#     i=i-1

# n=5
# i=1
# while(i<=n):
#     print(i*'*')
#     i=i+1

# j=n-1
# while(j>0):
#     print(j*'*')
#     j=j-1

# n=5
# i=1
# while(i<=5):
#     print((n-i)*" "+i*'*')
#     i=i+1
# j=n-1
# while(j>0):
#     print((n-j)*" "+ j*"*")
#     j=j-1


# n=5
# i=1
# while(i<=5):
#     print(i*"*")
#     i=i+1
# j=n-1
# while(j>0):
#     print((n-j)*" "+j*"*")
#     j=j-1

# n=5
# i=1
# while(i<=5):
#     print((n-i)*" "+ i*"*")
#     i=i+1
# j=n-1
# while(j>0):
#     print(j*"*")
#     j=j-1

# n=5
# i=1
# while(i<=5):
#     print((n-i)*" "+ i*"* ")
#     i=i+1
# j=n-1
# while(j>0):
#     print((n-j)*" "+j*"* ")
#     j=j-1

#    Calculator --------------------------------------------------

# while True:
#     print("1.for add\n 2.for sub\n 3.for multiply\n 4.for division\n 5.for Stop")
#     n=eval(input("enter the value"))
#     p=(1,2,3,4)
#     if n in p:
#         x=eval(input("enter the number1"))
#         y=eval(input("enter the number2"))

#         if n==1:
#             z=x+y
#             print(z)

#         elif n==2:
#             z=x-y
#             print(z)
        
#         elif n==3:
#             z=x*y
#             print(z)
        
#         elif n==4:
#             z=x/y
#             print(z)
        
#     elif n==5:
#             break
    
#     else:
#         print("invalid number")

# n=6
# m=8
# j=max(n,m)


# while True:
#     if(j%n==0 and j%m==0):
#         break
#     j=j+1
# print(j)

# l=["the","trop","bro"]
# print(' '.join(l))

# s="this is a string"
# print(s.split('a'))

# Factorial of a number -----------------------------------------------

# n=6
# i=1
# f=1
# while(i<=n):
#     f=f*i
#     i=i+1
# print(f)

#   number of vovels and consonenents in string -----------------------------

# s="aeiou"
# l=len(s)
# i=0
# t=('a','e','i','o','u','A','E','I','O','U')
# vovels=0
# consonents=0
# while(i<l):
#     if s[i] in t:
#         vovels=vovels+1
       
#     else:
#         consonents=consonents+1
#     i=i+1


# print(f'the total vovels is {vovels}')
# print(f'the total consonents is {consonents}')

# l=[10,20,30,40,50]
# ll=len(l)
# i=0
# while(i<ll):
#     l[i]=l[i]+5
#     i=i+1
# print(l)

# s="this is a string"
# l=s.split()
# print(l)

#  swapping without variable --------------------------------------------

# a=5
# b=6
# a,b=b,a
# print(a,b)

#   swapping with third variable ---------------------------------

# a=eval(input("enter first number"))
# b=eval(input("enter second number"))

# temp=a
# a=b
# b=temp
# print(b,a)

# area of triangle ----------------------------

# b=10
# h=20
# print((1*b*h)/2)

# area of square -------------------------------

# side=10
# print(side*side)

# square root of number -----------------------

# n=144
# i=1
# while True:
#     if(n==i*i):
#         print(i)
#         break
#     i=i+1

# for loops questions -----------------------------------------------

# x=range(1,11)
# for i in x:
#     print(i)

# n=5
# for i in range(1,11):
#     print(f'{n} * {i} = {n*i}')

# l=[10,20,30,40,50]
# for i in l:
#     print(i)

# n=2385098
# count=0
# while(n>0):
#     count=count+1
#     n=n//10
# print(count)

# Armstrong number -------------------------------------

# n=153
# x=n
# y=n
# count=0
# sum=0
# while(n>0):
#     count=count+1
#     n=n//10
# while(x>0):
#     m=x%10
#     sum=sum+m**count
#     x=x//10
# if(sum==y):
#     print(f'the numer {y} is armstrong')
# else:
#     print(f'the number {y} is not a armstrong number')

# s="string"
# l=len(s)
# x=''
# for i in range(l-1,-1,-1):
#     x=x+s[i]
# print(x)

#  How many even or odd in a collection 

# l=[1,2,3,4,5,6,7]
# odd=0
# even=0
# for i in l:
#     if (i%2==0):
#         even=even+1
#     else:
#         odd=odd+1
# print(f'even is {even}')
# print(f'odd is {odd}')

# n=10
# for i1 in range(1,n+1):
#     a=True

#     for i2 in range(2,i1):
#         if(i1%i2==0): 
#           a=False
#           break
#     if(a==True):
#         print(i1,end=' ')

#   except prime numbers print -----------------------   (imp)

# n=12
# for i1 in range(1,n+1):
#     a=True
#     if(i1==1):
#         print(i1,end=" ")
#         continue
#     for i2 in range(2,i1):
#         if(i1%i2==0):
#            a=False
#            break
#     if(a==False):
#         print(i1,end=" ")

    # fibonacci series with for loop --------------------------------------

# n=10
# f=0
# s=1
# print(f,end=" ")
# print(s,end=" ")
# for i in range(1,n-1,1):
#     n=f+s
#     print(n,end=" ")
#     f=s
#     s=n

#   fibonacci series with while loop --------------------------------------

# n=10
# f=0
# s=1
# i=1
# print(f)
# print(s)
# while(i<=(n-2)):
#     n=f+s
#     print(n)
#     f=s
#     s=n
#     i=i+1

# month="january"
# mdect={"january":31,"february":28,"march":30,"april":21,}
# if month in mdect:
#     print(f'{month} has this no of days {mdect[month]}')
# else:
#     print("invalid month name")

# d={
#     "name":"yash",
#     "class":10

# }
# print(d["name"])

#   Harshad number ----------------------------------

# n=19
# x=n
# sum=0
# while(n>0):
#   y=n%10
#   sum=sum+y
#   n=n//10

# if(x%sum==0):
#     print("harshad numberr")
# else:
#     print("not")

#   spy number ------------------------------------------------ 

# n=112
# x=n
# y=n
# sum=0
# pro=1
# while(n>0):
#     a=n%10
#     sum=sum+a
#     n=n//10
# while(x>0):
#     b=x%10
#     pro=pro*b
#     x=x//10
# if(sum==pro):
#     print("the number is spy number")
# else:
#     print("the number is not a spy number")

#    peterson number -----------------------------------------------------

# n=145
# x=n
# total=0
# while(n>0):
#     a=n%10
#     i=1
#     factorial=1
#     while(i<=a):
#         factorial=factorial*i
#         i=i+1
#     total=total+factorial
#     n=n//10

# if(x==total):
#     print("piterson")
# else:
#     print("not")

#   Neon --------------------------------------------------------

# n=12
# sq=n*n
# sum=0
# while(sq>0):
#     a=sq%10
#     sum=sum+a
#     sq=sq//10

# if(n==sum):
#     print("noen")
# else:
#     print("not")

  

# def add(x,y):
#     " this function is for addition of numbers"
#     return x+y
# z=add(4,5)
# print(add.__doc__) 

# def add(*n):
#     sum=0
#     for i in n:
#        sum=sum+i
#     return sum


# x=eval(input("enter"))
# y=add(*x)
# print(y)

# def show(**n):
#     print(n)
 
# y=eval(input("enter"))
# x=show(**y)
# print(x)

# l=["the","best","in","the"]
# x=' '.join(l)
# print(x)
# y=x.split()
# print(y)

d={"name":"yash","values":"yash"}
# print(d.values())

# print(d.keys())

# print(d.items())
# d.setdefault("fame","jadoo")
# print(d)

# d2={}
# d2.update(d)
# print(d2)

# print(d.pop("name"))
# print(d)

# s1={28,39,49}
# s1.update([1,2,3,4])
# print(s1)
# s1.discard(28)
# print(s1)
# s1.discard(28)
# print(s1)

#    Anagram program ------------------------------------------

# s1="python"
# s2="nohtjk"
# def anagram(s1,s2):
#     if(len(s1)!=len(s2)):
#         return "not"
    
#     count1=0
#     count2=0
    
#     for i in range(len(s1)):
#         char=s1[i]
    
        
#         for j in range(len(s1)):
#             if(char==s1[j]):
#                 count1=count1+1
            
#         for j in range(len(s2)):
#             if(char==s2[j]):
#                 count2=count2+1

#     if(count1==count2):
#         return "yes"
#     else:
#         return "not"

# x=anagram(s1,s2)
# print(x)

#    -------------------------------------------------------------------

# def is_anagram(s1,s2):
#     if(len(s1)!=len(s2)):
#         return "not"
    
#     count1=0
#     count2=0
#     for i in range(len(s1)):
#         char=s1[i]

#         for j in range(len(s1)):
#             if(char==s1[j]):
#                 count1=count1+1
#         for j in range(len(s2)):
#             if(char==s2[j]):
#                 count2=count2+1
#     if(count1==count2):
#         return "yes"
#     else:
#         return "no"
    
# s1="python"
# s2="nohtyp"
# x=is_anagram(s1,s2)
# print(x)

#   ------------------------------------------------------------------------

# n=eval(input("enter the number"))
# def add(x):
#     return x+1

# ans=map(add,n)
# print(list(ans)).


# def see(x):
#     a=''
#     a=x
#     return a

    

# inp1=eval(input("enter the list"))
# inp2=eval(input("enter the divisor"))

# print(inp1)
# print(inp2)
# ans=map(see,inp)
# print(list(ans))

# def to_str(x):
#     return str(x)

# ans=map(to_str,inp)
# print(list(ans))

# def mul(x):
#     return x*2
# ans=map(mul,inp)
# print(list(ans))

# def to_int(x):
#     return int(x)
# ans=map(to_int,inp)
# print(list(ans))

# def big(x):
#     return x.upper()


# ans=map(big,inp)
# print(list(ans))

# def check(x):
#     if(x%2==0):
#         return "even"
#     else:
#         return "odd"

# ans=map(check,inp)
# print(list(ans))

# def add(x,y):
#     return x+y
# ans=map(add,inp1,inp2)
# print(list(ans))

# def divi(x):
#     return (x//inp2, x%inp2)
# ans=map(divi,inp1)
# print(list(ans))

# def sq(x):
#     return x**2
# ans=map(sq,inp1)
# print(list(ans))

# l=[-1,2,3,-4,5,6,-7,8]

# def even(x):
#     if(x%2==0):
#         return "even"
# ans=filter(even,l)
# print(list(ans))

# def show(x):
#     if(x%2==0):
#         return "even"
#     else:
#         return "odd"
# ans=filter(show,l)
# print(list(ans))

# def ne(x):
#     if(x<0):
#         return x
# ans=filter(ne,l)
# print(list(ans))

# l=["yashA","youknow","YashB","perfect"]
# def five(x):
#     if(len(x)<=5):
#         return x
# ans=filter(five,l)
# print(list(ans))


# def my_name(x,y):
#     if(x==y):
#         return  x
#     elif (x>y):
#         return x
#     else:
#         return y
# ans=reduce(my_name,l)
# print(ans)

# l=["yashA","youknow","Peter Parker","John Cena"]
# def big(x,y):
#     if(len(x)==len(y)):
#         return x
#     elif(len(x)>len(y)):
#         return x
#     else:
#         return y
# ans=reduce(big,l)
# print(ans)

# def sm(x,y):
#     return x+y

# ans=reduce(sm,l)
# print(ans)



# def mx(x,y):
#     if(x==y):
#         return x
#     elif(x>y):
#         return y
#     else:
#         return x
# ans=reduce(mx,l)
# print(ans)

# from functools import reduce
# l=[2,15,6,18,18,10]

# def sm(x,y):
#     return x+y
# ans=reduce(sm,l)
# print(ans)

# lambda function 

# check=lambda x: "even number" if(x%2==0) else "odd Number"
# print(check(n))

# check=lambda x: "Zero" if(x==0) else ("Even Number" if (x%2==0) else "negative number")
# print(check(n))

# s=1
# k=4
# kb=5
# let=lambda x,z,y: [ [c for c in range(z,x+1)] for i in range(y)]
# print(let(k,s,kb))

# n="y"
# show=lambda x: [ x for i in range(1,6)]
# print(show(n))

# s=1
# e=5
# hm=5
# show=lambda x,y,z: [[ c for c in range(x,y+1)] for i in range(z)]
# print(show(s,e,hm))

# l=[]
# a=0
# for i in range(1,5):
#     l[a]="y"
#     a=a+1
# print(l)

# for _ in range(0,5):
#     print("hi")


l1=[1,2,3,4,5]

# ans=list(map(lambda x: x**2,l))
# print(ans)

# ans=map(lambda x: "even" if x%2==0 else "odd",l)
# print(list(ans))

# ans=map(lambda x,y: x**y,l,l1)
# print(list(ans))

l=[1,2,3,4,5]
# ans=filter(lambda a: a%2==0,l)    
# print(list(ans))

# from functools import reduce
# ans=reduce(lambda x,y: x if x>y else y,l)
# print(ans)

# show=lambda : [ [c for c in range(1,5)] for _ in range(4)] 
# print(show())

# p=[]
# for _ in range(5):
#     p.append("hii")
# print(p)

# l=["Ironman","captain america","Thor","an" ,"An"]
# let=filter(lambda x: x[0]=="a" or x[0]=="A",l)
# print(list(let))

# def even(x):
#     if(x%2==0):
#         return x
# ans=filter(even,l)
# print(list(ans))

# from functools import reduce

# def b(x,y):
#     if(x==y):
#         return x
#     elif(x>y):
#         return x
#     else:
#         return y
# ans=reduce(b,l)
# print(ans)

# def s(x,y):
#     return x+y
# ans=reduce(s,l)
# print(ans)

# def new():
#     yield 10
# print(new())
# print(list(new()))
# x=new()
# print(x.__next__())
# print(next(x))

# def even():
#     i=0
#     while(i<=10):
#         if(i%2==0):
#             yield i
#         i=i+1

# x=even()
# print(type(x))
# print(next(x))
# print((list(x)))
# print(x.__next__())
# print(next(x))
# print((list(x)))
# y=next(x)
# # print(y)
# for i in range(y):
#     print(i)
# z=next(x)
# for i in range(z):
#     print(i)
# for i in range(1,1):
#     print(i)
# print(list(x))
# print(list(x))
# for i in x:
#     print(i)

# def outer_fun(fun1):
#     def inner_fun():
#         print("Before Modification")
#         fun1()
#         print("After modification")
#     return inner_fun()

# def fun():
#     print("this is from main function")

# res=outer_fun(fun)
# res()

# def outer(fun1):
#     def inner():
#         print("before modification")
#         fun1()
#         print("after modification")
#     return inner

# def fun():
#     print("this is the main fuction")

# res=outer(fun)
# res()

# def outer(fun1):
#     def inner(x,y,z):
#         x=x+5
#         y=y+5
#         z=z+5
#         a=fun1(x,y,z)
#         print(a)
#     return inner


# def fun(x,y,z):
#     return x,y,z

# res=outer(fun)
# x=1
# y=2
# z=3
# res(x,y,z)

# print(x)
# print(y)
# print(z)

# def outer_fun(fun1):
#     def inner_fun(x,y,z):
#         x=x+5
#         y=y+5
#         z=z+5
#         a=fun1(x,y,z)
#         print(a)
#     return inner_fun


# def fun(x,y,z):
#     return x+y+z

# x=1
# y=2
# z=3

# res=outer_fun(fun)
# res(x,y,z)

# def outer(fun1):
#     def inner(x,y,z):
#         x=x+10
#         y=y+10
#         z=z+10
#         a=fun1(x,y,z)
#         print(a)
#     return inner

# def fun(x,y,z):
#     return x+y+z

# x=1
# y=2
# z=3
# res=outer(fun)
# res(x,y,z)

# print(x)
# print(y)
# print(z)

# def outer_fun(fuc1):
#     def inner_fun(name):
#         Print("this is before main function running")
#         result=fuc1(name)
#         return result.upper()
#     return inner_fun


# def fun(name):
#     print(f'Hello {name}')

# fun=outer_fun(fun)
# fun("yash")

# def outer_fun(fun):
#     def inner_fun(name):
#         print("before")
#         print(fun(name))        
#         return a.upper()
#     return inner_fun

# def fun(name):
#     print(f'Name: {name}')

# fun=outer_fun(fun)
# print(fun("yash"))


# def outer(fun1):
#     def inner(name):
#         a=fun1(name)
#         a.upper()
#         return a
#     return inner

# def fun(name):
#     print(f'Name: {name}')

# fun=outer(fun)
# print(fun("yash"))

# def outer(fuc1):
#     def inner(name):
#         print("before")
#         a=fuc1(name)
#         return a.upper()
#     return inner

# def fun(name):
#     return f'Hello {name}'

# fun=outer(fun)
# print(fun("yash"))

# def outer(fun1):
#     def inner(name):
#         print("before")
#         a=fun1(name)
#         return a.upper()
        
#     return inner


# def fun(name):
#     return f'Hello {name}'

# fun=outer(fun)
# print(fun("yash"))







