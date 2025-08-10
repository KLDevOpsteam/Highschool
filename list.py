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
    