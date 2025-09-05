# #print hello 5 times using while loop
# count = 1
# while count <= 5:
#     print('hello')
#     count += 1
# print('loop ended')

# # print numbers from 1 to 10
# i = 1  # iterator
# while i <= 10:
#     print(i)
#     i += 1   # iterization

# # print numbes from 10 to 1
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# #print prime numbers between 1 to 100
# num = 2
# while num <= 100:
#     if num % 2 != 0:
#         print(num)
    # num += 1

# # print element of te folloowing list using while loop
# my_lst = [1, 4, 9, 16, 35, 25, 49, 64, 81, 100]
# i = 0
# while i < len(my_lst):
#     print(my_lst[i])
#     i += 1

# # print multiplication table of a given number
# num = int(input("Enter a numver:"))
# i = 1
# while i <= 10:
#     print(num, 'x', i, '=', num*i)
#     i += 1

# Search a number x in this tuple loop
my_lst = [1, 4, 9, 16, 25, 36, 49, 9, 64, 81, 100]
x = int(input("Enter a number to search: "))
i = 0
while i < len(my_lst):
    if my_lst[i] == x:
        print("number found at index", i)
        break
    i += 1
else:
    print("number not found")
