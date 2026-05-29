marks=[]
count=0
flag=0
for i in range(5):
    mark=int(input("Enter the marks"))
    marks.append(mark)
    print(marks)
 
print("Highest mark is : ", max(marks))   
print("Lowest mark is : ", min(marks))
print("Average mark is : ",sum(marks)/len(marks))

for i in marks:
    if i>=40:
       count+=1
    else:
       flag+=1
print("Passed Student: ",count)
print("Failed Student: ",flag)   
