arr = [2,4,5,3,5,4,6]

sumOfEven=0
sumOfOdd =0

for digit in arr:
    if digit%2==0:
        sumOfEven+=digit

    else:
        sumOfOdd+=digit

print(sumOfEven)
print(sumOfOdd)