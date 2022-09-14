# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:34:12 2022

@author: banu
"""

# print("Banu Yasmeen")
# name="John Smith"
# age=20
# is_new=True
# input('what is your name?')

# name=input('Please enter your name')
# color=input('Enter the color you like')
# print(name + "likes"+color)

# weight_pd=input("enter your weight in pound:")
# type(weight_pd)
# weight_kg=float(weight_pd)*0.453592
# type(weight_kg)
# print('Your weight in kg is ' , weight_kg)

# is_hot=False
# is_cold=False

# if is_hot:
#     print("It's a hot day")
#     print("Drtink plenty of water")
    
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

# Price=1000000
# has_goodcredit=False
# if has_goodcredit:
#     print("you need tyo put down 10%")
#     downpayment=0.1*Price
#     print(F"you need to pay ${downpayment}")
# else:
#     print("you need tyo put down 20%")
#     downpayment=0.2*Price
#     print(F"you need to pay ${downpayment}")


# name=input("Please enter you name:")
# if (len(name)<3):
#     print("name must be atleast 3 characters")
# elif (len(name)>10):
#     print("name must be maximum of 10 character")
# else:
#     print("name looks good")

# weight=input("Plese enter your weight:")
# unit=input("(K)g or (L)b:")
# if(unit.upper()=="L"):
#     weight_kg=float(weight)*0.45
#     print(f"Your weight in kg is {weight_kg} pounds" )
# elif (unit.upper()=="K"):
#     weight_lb=float(weight)/0.453592
#     print(f"Your weight in nkg is {weight_lb}")
# else:
#     print("Enter weight greater than 0")

# i=5
# while(i>=0):
#     print('*' *i)
#     i=i-1
# print("Done")

# secret_no=9
# count=0
# limit=3
# while count<limit:
#     guess=int(input("guess"))
#     count+= 1
#     if guess==secret_no:
#         print("You win!!")
#         break
# else:
#      print("sorry you have failed")
    
# x=""
# start=False;
# stop=False
# while True:
#     x=input("> ").lower()
#     if(x=="start"):
#         if(start==False):
#             print("The car has started")
#             start=True
#         else:
#             print("The car has already started")
        
#     elif (x=="stop"):
#         if start==True:
#             print("The car has Stopped")
#             start=False
#         else:
#             print("the car has already stopped")
        
        
#     elif (x=="help"):
#         print("""
# Start - to start the car
# Stop - to Stop the car
# quit - to exit""")
#     elif(x=="quit"):
#         print("quitting")
#         break
#     else:
#         print("I don't understand that")

# prices=[10,20,30]
# total=0
# for i in prices:
#     total+=i
# print(f" total:{total}")

# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")

 #X in the shape of F 
 
# numbers=[5,2,5,2,2]
# for i in numbers:
#     print('*'*i ) ]

# X in the shape of L


# numbers=[3,3,3,3,8,9] 

# for i in numbers:
#     output='    '

#     for j in  range(i) :
#         output+='x'
#     print(output)

    #MAX

# l=[10,2,3,4,5]
# print(l)
# max=l[0]
# for i in l:
#    if(i>max):
#        max=i    
# print(max)      

#2- dimensional matrix  
# matrix=[
#         [1,2,3],
#         [4,5,6],
#         [7,8,9]
#         ]
    
# for row in matrix:
          
#    for item in row:
#        print(item)
# lists

# numbers=[1,2,3,4,6,3,7,8]
# numbers2=numbers.copy()
# print(numbers)
# numbers.append(20)
# print(numbers)
# numbers.insert(1,10)
# print(numbers)
# numbers.remove(2)
# print(numbers)
# numbers.pop(6) #- removes last item in a list
# print(numbers)
# print(numbers.index(4))
# #print(numbers.index(5)) #- valueError is returned if the value is not in list
# print(4 in numbers) #- prints boolean value and doesn't generate any error
# print(numbers.count(3))
# numbers.sort()
# print(numbers.reverse())

# #numbers.clear()
# print(numbers)

#Duplicate items in a list

# numbers=[1,2,3,2,3,1]
# numbers2=set(numbers)
# numbers=numbers2.copy()
# print(numbers)

numbers=[1,2,3,4,2,3,4,5,5,4,1]
numbers.sort()
for i in numbers:
    dup=numbers.count(i)
    
    if(dup>1):
          numbers.pop(i)
          
print(numbers)
    


    

    



