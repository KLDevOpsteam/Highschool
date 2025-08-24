# function = A block of reusable code
# def fun_name (parameters):  # defining a function
#        code
#        return variable  # return - used to end function. when function is called it will run the function code and return the mentioned value of variable to the caller.
# fun_name(enter arguments) # To call a function


def addition (num1,num2):
    sum= num1 + num2
    return sum

def multiplicaton (num1,num2):
    multiply= num1 * num2
    return multiply

def subtraction (num1,num2):
    subtract=num1-num2
    return subtract

def division (num1,num2):
    divide= num1/num2
    return divide

print(addition(1,2))
print(multiplicaton(3,2))
print(subtraction(6,2))
print(division(10,2))




#Default Arguments  = A default value for certain parameters. default is used when that argument is omitted.
# makes your functions more flexible , reduce no.of arguments.
# 1.Positional 2. DEFAULT 3.keyword 4.arbitrary


def net_price(listprice, discount=0, tax=0.01):  # giving default value for the 2 parameters.
    return listprice*(1-discount)*(1+tax)

#net_price(100) #If positional arguments not given it will give error. in function the parameter defined are 3, but argument given when calling the function is 1 hence gets error.
print(net_price(100,0,0.01))
print(net_price(100))# since we given default value to other 2 parameters it will take one argument without error.
print(net_price(100,0.1))# if we give any argument for the parameters which have default value, the function will take the argument valiue only.

#Exercise : count up program

import time

def count(end, start=0):
    for x in range (start,end+1):
        print(x)
        time.sleep(1)
    print("Time is up!")

count(3)



#keyword argument = An argument preceded by an identifier. helps with readability.
# order of arguments doesn't matter


def greet (greeting,title,name,surname):
    print(f"{greeting},{title}. {name} {surname}")


greet ("Hi",surname="smith",title="Mr", name="will") # Even if the argument is unordered if we use keyword it will take arguments correctly.
# Positional arguments should add before keyword argument.
# print(x,end=" ") end= is an keyword argument.
# print(x,sep="-") sep= is separator also a keyword argument.


# *args  = allows to pass multiple non-key arguments .# * args are taken as tuple.is a Positional arguments
# **kwargs  = allows to pass multiple keyword-arguments. # ** kwargs is taken as dictionary.
#  * unpacking operator

def sumof (*args):  # we can give multiple arguments for the functions,undefined no. of arguments.
    sum=0
    for arg in args:
        sum += arg
    print(sum)

def address (**kwargs):
    for key,value in kwargs.items():
        print(f"{key} --- {value}")

def label (*args,**kwargs):
    for arg in args:
        print (arg, end= " ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()
    print(f"{kwargs.get('name')}" )
    print (f"{kwargs.get('housename')}")


sumof(1,2,3,4)
sumof(2)
address (housename="vadakkeveettil",name="kunjunni",houseno="12B",district="kottayam")
label (1,2,3,4,housename="vadakkeveettil",name="kunjunni",houseno="12B")