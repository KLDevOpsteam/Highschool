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



#Logical Operators  - To evaluate Multiple conditions
#and - both condition must be true
#or - atleast one condition must be true
#not - inverse the condition --mostly in boolean




#String Methods


name="Anjana" 
print(len(name))  # to find the no.of letters in a string
print (name.find("j")) # variable.find("x") will give no. of letters till first occurance of x in the variable #output here is 2-an
print(name.rfind("n")) #variable.rfind("x") will give no. of letters till last occurance of x in the variable #output here is 4-anja
#if they could not find any letter the ouput will be -1.


# Capitalize
print(name.capitalize()) # caitalize() make first letter of the word capital.
print(name.upper()) # .upper() make all letters in upper case
print(name.lower()) # .lower() make all letters in lower case
print(name.isdigit())# isdigit is a boolean gives True or false. check the string contain only digits
print(name.isalpha())# returns True if string is only alphabetical
ipaddress="102.34.23.99."
print(ipaddress.count("2"))# count ("x") returns how many x in the string
ipaddress= ipaddress.replace("102","128") # .repace("x","y") To replace x from a string with y
print(ipaddress)


#Exercise 1 Validate user input

#username not more than 12 chara, not contain spaces, not contain digits
username= "g"
#username= input("Enter a username : ")
if len(username) > 12:
    print("Username should not contain more than 12 characters")
elif not username.find(" ") == -1:
    print("Username should not contain spaces")
elif not username.isalpha():
    print("Username should not contain digits")
else:
    print(f"{username} is accepted")






# Indexing = Accessing elements of a sequence using [] (indexing operator)
#[start:end:step]

phno= "9876543210" 
print(phno[3])
print(phno[0]) # indexing start with 0
print(phno[2:6]) # print from 3rd position to 7th position characters
print(phno[1:10:3]) # print from 1st position to lst position with alternative values: 97531
print(phno[-2])# [-x] give output last xth position
print(phno[::-1]) #print characters backward



#Format specifiers ={value:flags} format a value based on what flags are inserted

price1= 3.14321
price2 =-7654.98
price3= 44.67

print(f"price 1 is {price1:.2f}") # flag= :.xf   output the value with 2 decimal point of float
print (f"price 2 is {price2:9}") #flag= :x output will have x places by adding space infront of real value
print (f"price 3 is {price3:07}") # flag :0x   output will have x places by adding 0 infront of real value
print(f"price 1 is {price1:<9}") # flag :<x    output will have x places by adding space after the real value, align to the left
print (f"price 2 is {price2:>9}") # flag :>x    output will have x places by adding space infront the real value, align to the right
print (f"price 3 is {price3:^7}") # flag :^x    output will have x places by adding space infront and after the real value, align to the center
print (f"price 2 is {price2:+}") # flag :+ or : (space)   output with sign
print (f"price 2 is {price2:,}") #flag :, thousands place separated by ,
print (f"price 2 is {price2:<+,.2f}") # combination of flags




import time # Time library used for various operations

time.sleep(2) # it helps to delay the pgm to run for 2 seconds
print("time is up")

# Exercise  Countdown timer
import time

timer = int(input("Enter the count down time in seconds: "))

for t in range (timer,0, -1): # to count reversely we can give step as -1
    seconds = t % 60
    minutes =int(t/60)%60
    Hours= int(t/3600)
    print(f"{Hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time is up")

