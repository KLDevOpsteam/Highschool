print("I love Jesus")
print ("God Bless you")

#variable
#string, int,float,boolean
#string
name ="sara"
print (name)
print (f"sara") #f-string , format string literals
print (f"Hi {name}")# f{variable} 
Email = "sara4321@gmail.com"
print(f"Email of sara is {Email}")

#Integers
age = 20
print (age)
print (f"age of sara is {age} ")
Num_of_siblings=2
print(f"sara has {Num_of_siblings} siblings")

#float
Price_of_apple=99.9
Quantity=1.5
print(f"Sara bought {Quantity} kg of Apple with price Rs{Price_of_apple} per Kg")

#Boolean
#boolean has two values True or False; T & F always caps
is_student=True
is_employee =False
print (f"is sara a student?{is_student}")
print (f"Does sara work? {is_employee}")
#Boolean can be used inside a code like in if else 
if is_student:
    print("What is she studying")
else:
    print (f"Does sara work? {is_employee}")
for_sale=True
if for_sale:
    print("Item is for sale")
else:
    print("Item is Not available for sale")


# TypeCasting = converting a variable from one datatype to other
# str(),int(),float(), bool()
# command used to know the datatype of variable is "type"
print (type(name)) 
print(type(age))
print(type(Quantity))
print(type(is_student))

print(int(Quantity))#coverting float to int
print(float(age))#converting int to float

Num_of_siblings=str(Num_of_siblings)
print(Num_of_siblings)
print(type(Num_of_siblings))
Num_of_siblings +="0" #string concatenation only possible as Num of sibling changed to string.
print(Num_of_siblings)
#Num_of_siblings + 1 == Num_of_siblings        # As Num_of _sibling is not an integer anymore, it is string now.We can't do arithmetic operations/concatenate  this variable
#print(Num_of_siblings)

# string to bopolean
Name = "sid"
Name =bool(Name)
print(Name)# if the string is assigned to the variable the boolean will show True
Nickname = ""
Nickname=bool(Nickname)
print(Nickname)# If no string is assigned to variable it will give False
#We can use this to check whether we have assigned the string variable or not


#input()    prompts the user to enter the data, returns the entered data as a string.
#input("What is your Goal?")
Goal = input("what is your goal?")
print(f"your goal is {Goal}")
Age= input("your age?")
#Age == Age + 1 # input()data returns as string, so we can't concatenate the string assuming int.
print(Age)
print(type(age))
Age =int(Age) # to concatenate the variable as a integer ,we need to change the datatype of the variable from string to integer.
Age = Age + 1
print(Age)
print(type(age))
a=(int(input("Enter a Value")))# input changing to int by specifying the datatype int.
a=a+5 # No need to change the datatype,
print(a)
print(type(a))


