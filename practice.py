# even or odd program

# n=int(input('enter a number'))
# if n%2==0:
#     print('given number is even')

# else:
#     print('given number is odd')

# sum of digits

# num=int(input('enter a number'))
# numstr=str(num)
# sum=0
# for i in numstr:
#     sum=sum+int(i)
# print(sum)

# sum of digits

# num=int(input('enter a number'))
# x=num
# sum=0
# while x>0:
#     sum=sum+x%10
#     x=x//10
# print(sum)

# reverse a number

# num=int(input('enter a number'))
# x=num
# rev=0
# while x>0:
#     rev=rev*10+x%10
#     x=x//10

# print(rev)

# palindrom check

# num=int(input('enter a number'))
# x=num
# rev=0

# while x>0:
#     rev=rev*10+x%10
#     x=x//10

# if num==rev:
#     print('yes, the given number is palindorme')

# else:
#     print('not')

# factorial program

# num=int(input('enter a number'))
# total=1

# while num>0:
#     total=total*num
#     num=num-1

# print(f'factorial is {total}')

# factorial program

# num=int(input('enter a number'))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i

# print(fact)

# fibonacci series

# num=int(input('enter a number'))
# a,b=0,1
# for _ in range(num):
#     print(a,end=' ')
#     a,b=b,a+b

# counting how many digits a number is having

# num=int(input('enter a number'))
# count=0
# while num>0:
#     count=count+1
#     num=num//10

# print(count)

# Armstrong number

# num=int(input('enter a number'))
# x=y=num
# count=0
# sum=0
# while x>0:
#     count=count+1
#     x=x//10

# while y>0:
#     sum=sum+(y%10)**count
#     y=y//10

# if (num==sum):
#     print('armstrong')
# else:
#     print('not')

# swap two numbers (without temp)

# a,b=0,1
# a,b=b,a
# print(a,b)

# check palindrom string

# s=input('enter a string')
# if s==s[::-1]:
#     print('palindorm')
# else:
#     print('not')

# count vowels

# s=input('enter a string')
# vowels='aeiouAEIOU'
# count=0
# for i in s:
#     if i in vowels:
#         count=count+1
# print(count)

# remove spaces from string

# s='py th on'
# print(s.replace(' ',''))

# count chars of string

# s=input('enter a string')
# count=0
# for _ in s:
#     count=count+1

# print(count)

# count words in string

# s=input('enter a string')
# ss=s.split(" ")
# count=0
# for _ in ss:
#     count=count+1
# print(count)

# remove duplicate from string

# s=input('enter a string')
# see=''
# for i in s:
#     if i not in see:
#        see=see+i
# print(see)

# reversing words of a sentence

# s=input('enter a string')
# ss=s.split(" ")
# ss.reverse()
# s=" ".join(ss)
# print(s)

# swap first and last character

# s=input('enter a string')
# s=s[-1]+s[1:-1]+s[0]
# print(s)

# capitalize first and last character

# s=input('enter a string')
# s=s[0].upper() +s[1:-1] + s[-1].upper()
# print(s)

# maximum in a list

# lst=eval(input('enter a list'))
# max=0
# for i in lst:
#     if i>max:
#         max=i
# print(max)

# minimum in a list

# lst=eval(input('enter a list'))
# min=lst[0]
# for i in lst:
#     if i<min:
#         min=i
# print(min)

# remove duplicate from list

# lst=eval(input('enter a list'))
# lst1=[]
# for i in lst:
#     if i not in lst1:
#         lst1.append(i)
# print(lst1)

# Dictionary key search

# d={'a':1,'b':2}
# print('a' in d)

# # Dictionary value search
# print(2 in d.values())

# Mixing two dictionaries

# d1={'a':1}
# d2={'b':2}
# d1.update(d2)
# print(d1)

# swap dictionary keys and values

# d={'a':1,'b':2}
# newdict={v:k for k,v in d.items()}
# print(newdict)

# pattern

# n=int(input('enter a number'))
# for _ in range(n):
#     print('*'*n)

# pattern

# n=int(input('enter a number'))
# for i in range(1,n+1):
#     print('*'*i)

# pattern

# n=int(input('enter a number'))
# for i in range(n,1,-1):
#     print('*'*i)

# count character in a string

# s='yash'
# print(len(s))

# count words in a string

# s='yash is a boy'
# print(len(s.split(" ")))

# count the first non repeating character

# s='yash is a boy'
# for ch in s:
#     if s.count(ch)==1:
#         print(ch)
#         break

# check anagram

# s=input('enter a string')
# ss=input('enter a string')

# print(sorted(s)==sorted(ss))

# s=input('enter a string')
# print(s.replace(" ","-"))

# remove special character

# s=input('enter a string')
# ss=''
# for ch in s:
#     if ch.isalnum():
#         ss=ss+ch
# print(ss)

# check string contains only digit

# s=input('enter a string')
# print(s.isdigit())

# reverse words in sentence

# s=input('enter a sentence')
# ss=''
# a=s.split(' ')
# for i in a:
#     ss=i + " " + ss
# print(ss)

# find longest word in a sentence

# s='python programming is very interesting'
# a=s.split(' ')
# l=''
# for i in a:
#     if len(i)>len(l):
#         l=i
# print(l)

