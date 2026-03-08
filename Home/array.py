arr = list(map(int, input("Enter the array: "). split()))

sum =0
for i in arr:
    if i%2==0:
        sum+=i

print(sum)