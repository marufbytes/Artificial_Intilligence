num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int (input("Enter third number: "))

largest = num1

if num1<num2:
    largest=num2

elif num2<num3:
    largest=num3

print("Largest: ",largest)