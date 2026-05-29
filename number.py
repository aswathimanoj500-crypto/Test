numbers=[]
count=0
flag=0
for i in range(5):
    number=int(input("Enter the number"))
    numbers.append(number)
    print(numbers)
print("Largest number:",max(numbers))
print("Smallest number:",min(numbers))
print("Sum of number:",sum(numbers))
for i in numbers:
    z=i%2
    if z==0:
        count+=1 
    elif z!=0:
        flag+=1    
print("The count of even numbers are : ",count)        
print("The count of odd numbers are : ",flag)   