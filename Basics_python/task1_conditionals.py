# if statement( To print the no is even or odd)
num = int(input("enter a number"))
if num%2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# wap to print the greatest number
num1 = int(input("enter a number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number "))
if num1 > num2 & num1 > num3:
    print(num1,  "is greater")
elif num2 > num1 & num2 > num3:
    print(num2, "is greater")
else:
    print(num3,"is greater")