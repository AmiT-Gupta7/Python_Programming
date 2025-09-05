# # print esch element of the following list using for loop
# my_lst = [4, 9, 1, 27, 34, 48, 55, 63, 74, 82, 99]

# for item in my_lst:
#     print(item)


# # Search for a number x in this list using for loop
# x = int(input("Enter a number to search: "))
# for item in my_lst:
#     if item == x:
#         print(x,"Found..")
#         break
# else:
#     print(x,"Not found..")

# # print multiplication table of a given number
# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(num, "x", i, "=", num*i)

# # print the sum of first n natural numbers
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)

# # print factorial of a given number
# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1,num+1):
#     fact *= i
# print(fact)

# # print prime numbers between 1 to 100
# for num in range(2,101):
#     for i in range(2,num):
#         if num % i == 0:
#             break  # not a prime number
#     else:
#         print(num)

# pass statement
for i in range(1,11): 
    if i % 2 == 0:
        pass   # do nothing
    else:
        print(i)
        