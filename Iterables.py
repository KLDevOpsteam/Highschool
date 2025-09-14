#Iterables = An object /collection that can return its elements one at a time, allowing it to be iterated over in a loop.
number = [1,2,3,6,7,8]
for num in number:
    print(num)
print()
for num in reversed(number):
    print(num)


# List, Tuple, set(reverse won't work), string, dictionary  are Iterables



# Membership operators = used to test whether a avalue or variable is found in a sequence (string , list, tuple, set, or dictionary)
# Eg: in, not in

word= "fantastic"
letter= input("Guess a letter in word : ")
if letter in word:
    print(f"You guessed right, there is {letter} in word")
else:
    print(f"Oops, there is no {letter} in word")

students={"Anjana","Anu","priya","malu"}
student=input("Enter the student name : ")
if student not in students:
    print(f"{student} is not found")
else:
    print(f"{student} is present")

grades = {"Anjana":"A","Anu":"B","priya":"B","Malu":"A"}
girl =input("Enter the student name : ")
if girl in grades:
    print(f"Grade of {girl} is {grades[girl]}")  # to get valye of dictionary specifically for a key in dictionary
else:
    print(f"{girl} is not present")



#List Comprehension = A concise way to create lists in python. Compact and easier to read than traditional loops.[expression for value in iterable if condition]

doubles= []
for x in range(1,11):
    doubles.append(x*2)
print(doubles)

triples=[x*3 for x in range (1,11) ]  #expression (action needs to do) = x*3, value = x, iterable is range= in range (1,11)
print(triples)

num=[1,-2,3,-6,0,9]
positive_num = [x for x in num if x>=0]
print(positive_num)

#Match-case statement(switch): An alternative to using many 'elif' statements.Execute some code if a value matches a 'case' 


def week(days):
    match days:
        case 1:
            print("Sunday")
        case 2:
            print("mon")
        case 3:
            print("Tue")
        case 4:
            print("Wed")
        case 5:
            print("Thu")
        case 6:
            print("Fri")
        case 7:
            print("Sat")
        case _:              # case _ is wild card, replacement of else.
            print("Invalid")
print(week(7))

def weekend(day):
    match day:
        case "sun" | "sat":
            print("Weekend")
        case "mon"|"tue"|"wed"|"thu"|"fri":
            print("Weekday")
        case _:              # case _ is wild card, replacement of else.
            print("Invalid")

print(weekend("thu"))

# Module = a  file containing code you want to include in your program use 'import' to include a module (built in or your own). Useful to break up a large program reusable separate files.
# print(help("modules"))
#import math  # to include the module in pgm import used.
# module.function/values  
#import math as m  # importing math module aliasing with m, we can use m instead of math.
#from modulename import function/value

# create our own Module ---> write click on folder > new  > give name for module > python file

import TestModule
print(TestModule.pi)
print(TestModule.area(7))
print(TestModule.cube(3))

#variable scope = where a variable  is visible and accessible 
# scope resolution =(LEGB)Local>Enclosed>Global>Built-in
#Local Variable  -- defined within function and works within the function
#Enclosed variable -- When a function defined in another function.
# Global variable -- outside of any function
#built in variable -- from modules
