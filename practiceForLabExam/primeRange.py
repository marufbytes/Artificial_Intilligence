num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))

for num in range(num1, num2+1):
    if num<=1:
        continue
    
    else:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num, end=' ')

