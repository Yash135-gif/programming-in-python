# class Student:
#     '''Student detail'''
#     name="yash"
#     age=20

# print(dir(Student))

# print(Student__doc__)

# print(Student)
# obj=Student

# obj=Student()
# print(obj)


# class Student:
#     '''Student detail'''

#     def __init__(self):
#         print("Constructor Called")
#         print(id(self))

# obj=Student
# obj=Student()

# print(id(obj))

# class Student:
#     '''Student detail'''

#     def __init__(self,name,roll,marks):
#         self.x=name
#         self.y=roll
#         self.z=marks

# obj=Student("yash",27,80)
# print(obj.x)
# print(obj.y)
# print(obj.z)

# class Student:
#     '''Student detail'''

#     def __init__(self,name,roll,marks):
#            self.x=name
#            self.y=roll
#            self.z=marks

#     def __init__ (self):
#         print("construcor called")
    

# obj=Student()
# obj.__init__()

    # I M P  ----------------------------------------------------------

# class Student:
#     def __init__(self,name,roll,marks):
#         self.x=name
#         self.y=roll
#         self.z=marks

#     def add_new(self,city):
#         self.c=city

#     def show(self):
#         print(self.x,self.y,self.z,self.c,self.school_name)

# obj1=Student("yash",20,90)
# obj1.add_new("bhopal")
# obj1.school_name="STJP"
# obj1.show()

# print(obj1.x,obj1.y,obj1.z,obj1.c,obj1.school_name)

#   IMP 
 
class Sports:
    def __init__(self,name1,name2,name3):
        self.a=name1
        self.b=name2
        self.c=name3

    def add_player(self,name4,name5):
        self.d=name4
        self.e=name5
    def display(self):
        print(self.a,self.b,self.c,self.d,self.e,self.manager)

obj1=Sports("messi","abd","sky")
obj1.add_player("alien","musiala")
obj1.manager="Pep"
obj1.display()




        
