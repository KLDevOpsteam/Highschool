l=[]
len =5
for i in range (len):
    l.append(i)
print (l)


l=[]
len=int(input("Enter a number"))
for i in range (len):
    l.append (int(input("Enter a value")))
    print (l)
sum=0
for i in l:
    sum=sum+i
print (sum)




#Collection = single "variable" used to store multiple values.
#List[] = ordered and changeable, duplicates ok
# set {} = unordered and immutable , add/ remove is ok, no duplicates
# Tuple () = ordered and unchangeable , duplicates ok. faster than list

fruit = ["Apple","orange","banana","pears","cherry"]#List
print (fruit[0])
print (fruit[1:3]) # print 1 to 3 positioned values in the list
print (fruit[:3]) # print from start till 3rd position values
print (fruit[::2])# from start to end with alternative ie. step 2 will be printed.
print (fruit[::-1])# print reverse order


print("laddu" in fruit) #  in listname operator it is like a boolean if present it gives true else false, can use to check anything in a list.
fruit[3]="grapes" # can replace a variable in list by assignment.
fruit.append("pears")# To add element to the end of the list
fruit.remove("orange") # To remove any element from the list
fruit.insert(1,"orange") # To add an element in the particular position.
fruit.sort() # to sort elements in alphabetical order
fruit.reverse()# to reverse the order
#fruit.clear() # to clear all elements in a list
print(fruit.count("Apple")) # to count the specific element in a list.
print(fruit.index("cherry"))
print(fruit)


#print (dir(list)) to show all attributes and functions of list
# print (help(list)) to show all details of list
fruits = {"Apple","orange","banana","pears","cherry"} #Set
fruits.add("fig")# To add element to set
fruits.remove("pears")# To remove an element from set
fruits.pop()# to change the elements in first to other position
print(fruits)
#index operator [start:stop:step] can't use in set as it is unordered.



froots = ("Apple","orange","banana","pears","cherry") #Tuple
print(froots)


#Exercise : Shopping cart program
items=[]
prices =[]
quantities=[]
while True:
    Items=input("Enter the items to buy: (q for quit)")
    if Items.lower() == "q":
        break
    else:
        price=float(input (f"price of {Items}?"))
        quantity=int(input("Enter the no.of packets needed"))
        items.append(Items)
        prices.append(price)
        quantities.append(quantity)
print ("Your cart !!") 
print ()

for Item,quantity,price in zip(items,quantities,prices):
        print(f"{Item:<10}{quantity:<14}{price}")
TotalAmount=0
for quantity,price in zip(quantities,prices):
    Total = quantity*price
    TotalAmount += Total

print ("Total Amount to pay =",TotalAmount)


#2D collections --Like a table

#Exercise : Number pad

num_pad1 =  (1,2,3)
num_pad2=   (4,5,6)
num_pad3=   (7,8,9)
num_pad4=   ("#",0,"*")

#Aligned each tuple orderly makes each tuple as an element in num_pad
#num_pad=( (1,2,3),(4,5,6),(7,8,9),("#",0,"*"))     this one also give same output as below .making 2d collection in one sentance
#can make 2D collection with [],(),{}
num_pad=(num_pad1,num_pad2,num_pad3,num_pad4)
#print(num_pad[0][1])    it will give output as 1st row 2nd element.
#for x in num_pad:
#     for y in x:
#          print(y) #this will give output of each elements in tuple.
#           print(y,end=" ")
#      print() # this will give each tuple in line
    
for numbers in num_pad:
    for num in numbers:
        print(num,end=" ")
    print()


#Exercise  Python quize Game

Questions=("How many continents are present?","which flower is biggest in the world","Which day is celebrated as Environmental Day")
Options=(("A.7","B.4","C.9"),("A.Rose","B.orchid","C.Rufflasia"),("A.June10","B.Jul5","C.March12"))
answers=("A","C","B")
guesses=[]
score=0
question_num=0

for question in Questions:
    print(question)
    for option in Options[question_num]:
        print(option)
    guess= input("Enter the answer(A,B,C): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
            score += 1
            print("Correct")
    else:
         print("Incorrect")
         print(f"Correct Answer is {answers[question_num]}")
    question_num += 1   
print(f"Your score is {score} ")


#dictionary = A collection of {key:value} pairs . ordered and changeable .No duplicates.

capitals={"KL":"TVM","TN":"CHN","AP":"Amaravathi","KA":"Banglore"}
# print(dir(capital))  #shows attributes and methods
# print(help(capitals))  #indepth details

print(capitals.get("KL"))  #get can be used to find the pair of given key
#print(capitals.get("CHN"))  #we can use only key with .get
print(capitals.get("Goa"))  # as Goa is not mentioned in dictionary , it will output "None"
capitals.update({"Bihar":"Patna"}) # .update used to add key-value to dictionary also to change any existing value.
capitals.update({"AP":"AMR"})
capitals.pop("KA") # .pop used to remove key-value from a dictionary.
capitals.popitem() # .popitem() will remove latest added Key- value.
#capitals.clear()  #.clear() will empty the dictionary.
print(capitals)

print(capitals.keys()) # .keys will output only keys mentioned in dictionary.
#for keys in capitals.keys() to iterate keys in a given dictionary 
print(capitals.values()) # .values will output only values in the dictionary.
print(capitals.items())  # it will give the keys and values in a dictionary as a 2D list
for key, value in capitals.items():
     print (f"{key} - {value}")    # helps to print key and value as a table.


#Exercise : Menu  Display

menu={"Menu":"Price in","Panipuri": 30.00,"Bhelpuri":40.00,"Masalapuri":45.00}
print("   TODAY'S CHATTS!!   ")
print()
for puri,price in menu.items():
     print (f"{puri:^10}  {price:^10} Rs")
print()
print("    Enjoy the Flavour    ")

cart=[]
Total=0
while True:
        chatts=input("Enter the chatt you want (Type quit to Exit) : ").capitalize()
        if chatts=="Quit":
           break
        elif menu.get(chatts) is None:
             print ("Sorry, the selected item is not available")
        else:
            cart.append(chatts)
#print(cart)
#print(type(menu.get(chatts)))
for chatts in cart:
     Total += (menu.get(chatts))
print(f"Total Amount to pay = {Total}")
