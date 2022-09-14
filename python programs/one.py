# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:11:03 2022

@author: banu
"""
# a=100
# b=300
# if a>b:
#     print("a is greater than b")
# elif a==b:
#     print("a is equal to b")
# else:
#     print("b is greater than a")
# i=int(input("Please enter an integer"))


# while i>0 :
#         print("The integer you have entered is a positive and is greater than 0")
    
#         if (i%5==0) and (i%3==0):
#             print("The integer is divisible by both 5 and 3")
#             break
#         elif(i%2==0):
#             print("The integer is divsible by 2")
#             break
#         else:
#             print("ITs not divisible by 2,3 and 5")
#             break
# else:
#         print("you have entered a negative number!! please enter positive number")
        
        
# tup=("BMW","BENZ","FERRARI","AUDI") 
# for x in tup :
#     print(x)
     

# employee={"Name":'Banu',"age":25,"Salary":80000}
# print(employee)
# print(len(employee))

# a,b=50,100.0053
# print(id(a))
# a=1
# print(id(a))
# print(a,b)

# (x,y,z)=5.677,"K1G4b5",-9
# (a,b,c)=(type(x),type(y),type(z))
# print(a,b,c)

# (a,b,c)=(10,10,10)
# x=y=z=10
# print(a,b,c,x,y,z)

     
       # DATA TYPES
 #Numeric
# num=7
# floa=4.687
# com=3+8j
# stri="banu"
# r=True
# if num>(int(floa)):
#     print("great")
    
# print(type(num))
# print(type(floa))
# print(type(com))
# print(com.real)
# print(com.imag)
# print(int(floa))
# print(stri+str(num)) 
# # can add num to string by converting it 
# #into string but can't convert str to int
# print(int(floa))

# str1="hi"
# str2="python"
# print(str1+str2)
# print(str2[1])
# print(str2.find("o"))
#List
# split1="this is orange"
# l1=(split1.split(" "))
# l2=["hi","hello"]
# l3=l1+l2
# print(l3) 
#tuple
# tup=("abc","frf")
# tup2=("snnnn","jbnsl")
# tup=tup+tup2
# print(tup*2)
#mapping- dic
# dic={1:"banu",2:"two",3:"hi"}
# print(len(dic))
# set1={'a','b','c','d',3,4,5}
# set2={1,2,3,4,5,}
# print(set1|set2)
# print(set1&set2)
#range
# a=range(9)
# b=range(2,7)
# c=range(1,10,3)
# for x in a:
#     print("a",x)
#     for y in b:
#         print("b",y)
#         for z in c:
#             print("c",z)

# s="hello! good Morning!!"
# print(s)
# print(type(s))

# l=list(s)
# print(l)
# print(type(l))

# s1=set(l)
# print(s1)
# print(type(s1))
# s2=set(s)
# print(s2)
# print(type(s2))

# t=tuple(s)
# print(t)
# print(type(t))
# t1=tuple(l)
# print(type(t1))
# t2=tuple(s1)
# print(t2)
# print(type(t2))
# t3=t1+t2
# print(t3)

# a=0b101
# t=0o11
# c=0x12
# print(a)
# print(type(a))
# print(t)
# print(type(t))
# print(c)
# print(type(c))


#Fraction

# from fractions import Fraction as F
# print(F(1,3))
# print(F(1,3)+F(1,3))
# print(1/F(5,6))

#functions
#Absolute function - prints the positive value of the integer
# v=-43.90
# print(abs(v))
# print(max(1,409,299,940,1000))
# print(min(1,409,299,940,1000))

# import math
# print(math.pi)# Prints Pi value
# print(math.e)
# print(math.exp(10))
# print(math.log10(1000))
# print(math.factorial(5))
# print(math.sqrt(100))
# print(math.ceil(593.890))
# print(math.ceil(593.40))
# print(math.floor(593.890))
# print(math.pow(2,6))
# print(math.cos(0))
# print(math.cos(math.pi ))
# print(math.tan(0))
# print(math.tan(math.pi/4))

# import random
# print(random.randrange(10,20)) # Keeps generating the random integer from the given range

# x=(5,6,3,5,3,2,1)
# print(random.choice(x))# keeps choosing  the random integer in x 

#ord function accepts a string of unit length and returns the unicode equivalence of the past argument



# employee={"Name":'Banu',"age":25,"Salary":80000}
# print(employee.keys())
# print(employee.values())
# print(employee)
# employee["education"]="Meng"
# print(employee)
# t1=(1,2,3)
# print(t1)
# t1=t1+(4,5)

# print(type(t1))
# s=(1,2,3)
# s=s+(4,5)
# print(s)

# #File objects
# f1=open('C:/Users/banu/OneDrive/Desktop/pythontest/test.txt','w')
# f1.write("Hello Welcome to python programming")
# f1.close() 

# #Sets
# s=set('INDIA')
# s1=set('USA')
# print(s,s1)
# print(s&s1)
# print(s|s1)
# str1="hello Programmer! Welcome!!"
# print(str1[::-1])
# print('a 'in str1)

#format

print("hello {}".format("Banu"))
print("Hello{1} and {0}".format("hi","hello"))
print("Hello{0} and {1}".format("hi","hello"))
print("Hello{a} and {b}".format(a="hi",b="hello"))
name="Banu Yasmeen"
salary=90000
print("Her name is %s\n Her salary is %d"%(name,salary))


def greeting(x):
    print("hello ",x.capitalize())
    print("hello",x.casefold())
    print("hello",x.upper())
    print("hello",x.lower())
    print("hello",x.title())

name=input("Please name")
greeting(name)
greeting("banu")
# number=int(input("Please enter the number you would like to check"))
# if number>1:
#     for i in range(2,int(number/2)+1):
#         if (number%i)==0:
#             print(number,"The Number you hav entered is not prime")
#             break
            
#         else:
#             print("The number you have entered is prime")
            
# else:
#     print("The n'the umber you have entered is not prime")