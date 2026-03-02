digit = [2,4,5,7,4,7,4,5,8,2,4,6,5,5]
sum=0
for x in digit:
    if x%2==0:
        sum+=x

print("Sum: ",sum)