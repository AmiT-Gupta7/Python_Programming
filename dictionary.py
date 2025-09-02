my_dict = {"name": "Amit", "age": 21, "city": "gkp"}

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.get("age"))

# my_dict.update({"country": "india",})
# print(my_dict)

# my_dict.update({"city":"delhi"})

# # my_dict.pop("city")
# print(my_dict)

my_dict2 ={}

n = int(input("Enter number of subjects: "))
for i in range(n):
    subjet = input("Enter your subject: ")
    marks = float(input("Enter your marks: "))
    
    my_dict2.update({subjet:marks})
print(my_dict2)

