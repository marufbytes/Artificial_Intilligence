num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def is_prime(n):
    if n<2:
        return False
    
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print(f"\n Prime number between {num1} and {num2}:")

for num in range(num1,num2+1):
    if is_prime(num):
        print(num, end=' ')

print()

