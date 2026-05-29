thislist=[]
mylist=[]
for i in range(5):  
   x=int(input("Enter 5 numbers"))
   thislist.append(x)
   
for n in range(5):   
   y=int(input("Enter 5 numbers"))
   mylist.append(y)

set1=set(thislist)  
set2=set(mylist) 
print("Set 1 is: ",set1)
print("Set 2 is: ",set2)
set3=set1.intersection(set2)
print(set3)