x=range(1,21)
for y in x:
    if y%3==0:
        continue
    if y==15:
        break
    print(y)
    