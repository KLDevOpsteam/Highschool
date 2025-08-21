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