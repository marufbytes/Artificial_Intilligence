num = int(input("Enter a number: "))

if num==0 or num==1:
    print("The number is not prime")

elif num>0:
    for i in range(2,num):
        if num%i==0:
            print("Number is not Prime number")
            break
        else:
            print("The number is prime")