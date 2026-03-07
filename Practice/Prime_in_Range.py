start = 10
end = 20

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)


num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

for num in range(num1, num2+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)