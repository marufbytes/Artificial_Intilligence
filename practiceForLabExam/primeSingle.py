num = int(input("Enter the digit: "))

if num<=1:
    print("Not prime")

else:
    for i in range(2,num):
        if num%i ==0:
            print("Not prime Number")
            break

        else:
            print("Prime Number!")
            break
