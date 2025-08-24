


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





#conditional expression
# A one line shortcut for the if statement(tenary operator )
#print or assign one of two values based on a condition
# x if condition else y

Num =3
print("positive" if Num > 0 else "Negative")
Num =-9
print("positive" if Num > 0 else "Negative")
Num = 3
print ("Even" if Num%2==0 else "odd")
Num=8
print ("Even" if Num%2==0 else "odd")
Num1=4
Num2=3
print(f"greater Num={Num1}" if Num1>Num2 else f"greater Num ={Num2}" )



#While loop = execute some code till some conditions remains True

Number = int(input("Enter a num(0 for quit)"))

while not Number == 0:
    print(Number)
    Number = int(input("Another number:"))
print("quit")



#Exercise : Compound Interest Calculator

while True:   # True is used in while as condition , it will run infinitely , we need to use "break" at the end of while loop.
    principle = float(input("Enter the principle"))
    if principle <=0:
        print ("Principle should be greater than 0")
    else:
        break
Years = int(input("Enter years of deposit: "))
while True:
    Rate = float(input("Enter the rate of interest= "))
    if Rate <=0:
        print ("Rate of interset should be greater than 0")
        
    else:
       break

i=Years
while i>0:
    Amount=principle + (principle*Rate)/100
    principle=Amount
    i -= 1
print(f"Amount receive after {Years} years is {Amount:.3f}")


# For loops = Execute a block of code a fixed number of times. can iterate over a range , string, sequence etc.

for x in range (1,11):
    print(x)
for x in reversed(range(1,11)): # reversed halp to iterate in reverse direction
    print(x)
print("End of For loop")

for x in range (1,11,3): # u can add step also ,it is incrementing by the step value
    print(x)

phNo="999-678-7789"
for i in phNo:
    print(i)

for x in range (1,11):
    if x==5:
        continue # continue is another term like break, here 5 will be skipped.
    elif x==9:
        break  # break is used to come out of the iteration and stop the running of code.  Till 8 output will print remaining will be skipped.
    else:
        print(x)



#Nested Loop = A loop within another loop(outer, inner)
#outer loop:
   # inner loop:


for x in range (5):
    for y in range (1,21):
        print (y, end =" ")
    print() # this helps to print new line after each iteration


for x in range (5):
    for y in range (5):
        print ("<>",end="")
    print()




# Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop.

numbers=[1,2,3,4,5]
evens=(2,4,6,8)
vowels={"a","e","i","o","u"}
my_dictionary={"one":1, "Two":2, "Three":3}
for num in reversed(numbers):  # to print in reverse order.
    print (num,end=" ")
for even in evens:
    print(even,end=" ")
for vowel in (vowels):  #reverse wont work here because set is unordered.
    print(vowel,end=" ")
for keys in my_dictionary.keys():
    print(keys,end=" ")