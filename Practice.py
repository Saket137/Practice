               #PYTHON PRACTICE
                   


#Addition
a=10
b=20
print(a+b)

#Substration
b=20
a=10
print(b-a)

#Current Date and Time
import datetime
from fileinput import filename
from typing import List, Tuple
now=datetime.datetime.now()
print("Curren Date and Time is:"+now.strftime("%Y-%m-%d %H: %M:%S"))

#Area of Circle
r=114
area=3.14*r*r
print(area)

#Area of Circle with user input
r= float(input("The Radius of Circle: "))
print("The area of circle with radius: "+str(r)+" is "+str(3.14*r*r))


#Print First name and last name by user input
name1= str(input("First Name : "))
name2= str(input("Last Name: "))
print("Name is: "+name2+" "+name1)


#Reverse string



#List and Tuple

numbers=input("Enter the numbers with comma: ")
list=numbers.split()
tuple=tuple(list)
print("List: ",list)
print("Tuple:",tuple)



#**********
#important*
#**********

#Print Extension of Filename
name=input("Enter the file name: ")
f_extns=name.split(".")
print("File extension is; "+repr(f_extns[-1]))









values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

