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





    
