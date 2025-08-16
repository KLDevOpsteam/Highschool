#Arithmetic Operators
#+,=,-,*,/,%

a=0
a=a+1
a += 1 #Augmented assignment 
print(a)
b=3
b=b-1
b -= 1
print(b)
c=4
print(a*b*c)
c *=2
print(c)
d=10
d =d**3 # ** raised to
print(d)
print(d/a)
e=12
e /= 2
e =e**2 #Power of a number **
print(e)
Remainder =e%5 # divides and gives remainder
print(Remainder)



#Arithmetic functions
# round(x),abs(x), pow(x,y), max(x,y,z), min(x,y,z)

l=8.96
n=7
m = round(l)
print (round(l*n))
r=-5

print(abs(r))# abs() gives the positive value of a negative value or how far that no from 0.
f=2
g=4
print (pow(f,g))# pow(x,y) gives x^y ,x power of y
print (max(l,n,m,r,f,g)) # max() To find max value from a set of values
print (min(l,n,m,r,f,g))# min() To find min value from a set of values



# we can use math library for various math operations, for that use import math

import math

print(math.pi)
print(math.e)
print(math.sqrt(9))
print(math.ceil(9.1)) # round a number up.Eg: 9.1 to 10
print(math.floor(9.1))# round a number down . Eg :9.1 to 9



#Exercise 1 Calculating circumferrance of circle using math library.
import math
radius=float(input("Enter the radius of the circle"))
print(f"circumferance of the circle = {round(math.pi*2*radius,2)}") # round(x,2) round the value of x to 2 decimal point.


#Exercise 2 Calculating area of the circle
import math
Radius=float(input("Enter the radius of the circle"))
print (f"Area of the circle  is {round(math.pi*pow(Radius,2),3)}cm^2")

#Exercise 3 Hypotenuse of triangle
import math
length =float(input("Enter length  of the triangle"))
breadth = float(input("Enter breadth of the triangle"))
print(f"Hypotenuse of the triangle is {round(math.sqrt(pow(length,2)+pow(breadth,2)),2)}cm")






# if -elseif- else condition
# can use boolean in if statement.

s= int(input("Enter a value"))
if s>=5:
    print(s)
elif s==2: # == is comparison operator ,= used for assigning.
    print("2")
else:
    print("NA")

# Exercise 1 Python calculator

operation=input("Please enter which mathematical operations you want to do?(+,-.*,/)")
Value1 = float(input("Enter the value"))
Value2 = float(input("Enter the 2nd value"))

if operation == "+":
    Answer = Value1 + Value2
    print(round(Answer,3))
elif operation == "-":
    Answer = Value1 - Value2
    print(round(Answer,3))
elif operation == "*":
    Answer = Value1*Value2
    print(round(Answer,3))
elif operation == "/":
        Answer=Value1/Value2
        print(round(Answer,3))
else:
    print("Enter a valid operator")

