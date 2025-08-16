#Logical Operators  - To evaluate Multiple conditions
#and - both condition must be true
#or - atleast one condition must be true
#not - inverse the condition --mostly in boolean


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



#While loop = execute some code till some conditions remains True

Number = int(input("Enter a num(0 for quit)"))

while not Number == 0:
    print(Number)
    Number = int(input("Another number:"))
print("quit")

    