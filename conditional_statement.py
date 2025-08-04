# WAP to check the number is even or odd.
num = int(input("Enter a number :"))

if (num % 2 == 0):
    print("Number is even...")
else:
    print("Number is odd...")


# WAP to find the greatest of 3 number enter by the user.
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))

if (num1 >= num2 and num1 >= num3):
    print(num1,"first number is greater...")
elif(num2 >= num1 and num2 >= num3):
    print(num2,"second number is greater...")
else:
    print(num3,"third number is greater...")


# WAP to check the number is even or odd.
num = int(input("Enter a number :"))

if (num % 7 ==0):
    print("Number is Multiple of 7...")
else:
    print("Not Multiple of 7...")