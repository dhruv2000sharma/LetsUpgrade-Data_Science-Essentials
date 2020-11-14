# Name : DHRUV SHARMA
# Assignment no : 2(Que 2)

# Questions 2:
# Create a notebook on LIST COMPREHENSION. This exercise is to put you in a Self learning mode

my_list = []  # empty list creates
print("print empty list :", my_list)

my_list1 = [10, 20, 15, 68, 9, 56, 85, 95, 64, 58, 56, 32, 32]  # int List create

print("List of int :", my_list1)

mixed_list = [10, 'yogi', 20.0, "Pune"]
print("mixed list is :", mixed_list)

print('X' * 50)  # indication purpose

from collections import Counter

list = [1, 2, 3, 4, 5, 3, 2, 3, 4, 5, 6, 5, 4, 6, 7, 8, 9, 0, 7, 6, 5, 4, 6, 7, 7, 9]

print(Counter(list))

str = 'I am yogi Halagunaki and i am from pune itself and i am doing cdac in Data science '

word_list = str.split()

print(Counter(word_list))

print('X'*50)

# print(my_list.append(10))

print(my_list1.append(mixed_list))
print(my_list1[1])
print(my_list1[:3])
print(my_list1[3:])
# print(my_list1.count())
print('X'*50)

print(mixed_list)
mixed_list.remove(mixed_list[2])
print(mixed_list)

mixed_list.append("Teju")
my_list1.append("Ashu")
print(mixed_list)

print(my_list1)
my_list1.remove(my_list1[3])
print(my_list1)

print('X'*50)


my_list.append(13)
my_list.append(11)
my_list.append(1)
my_list.append(2)
my_list.append(20)
my_list.append(17)

print(my_list)

my_list.remove(my_list[3])

print(my_list)

print("Unsorted list :",list)
list.sort()
print("Sorted list :",list)
print('X'* 50)
print("Sum of list  is :",sum(list))

print("ASCII : :",ascii(list))

#
# Output :
# /home/yogi/Desktop/Python_Code/venv/bin/python /home/yogi/Desktop/Python_Code/Lets_Upgrade_Assignments/day2/Day2_Que2.py
# print empty list : []
# List of int : [10, 20, 15, 68, 9, 56, 85, 95, 64, 58, 56, 32, 32]
# mixed list is : [10, 'yogi', 20.0, 'Pune']
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Counter({4: 4, 5: 4, 6: 4, 7: 4, 3: 3, 2: 2, 9: 2, 1: 1, 8: 1, 0: 1})
# Counter({'am': 3, 'and': 2, 'i': 2, 'I': 1, 'yogi': 1, 'Halagunaki': 1, 'from': 1, 'pune': 1, 'itself': 1, 'doing': 1, 'cdac': 1, 'in': 1, 'Data': 1, 'science': 1})
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# None
# 20
# [10, 20, 15]
# [68, 9, 56, 85, 95, 64, 58, 56, 32, 32, [10, 'yogi', 20.0, 'Pune']]
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# [10, 'yogi', 20.0, 'Pune']
# [10, 'yogi', 'Pune']
# [10, 'yogi', 'Pune', 'Teju']
# [10, 20, 15, 68, 9, 56, 85, 95, 64, 58, 56, 32, 32, [10, 'yogi', 'Pune', 'Teju'], 'Ashu']
# [10, 20, 15, 9, 56, 85, 95, 64, 58, 56, 32, 32, [10, 'yogi', 'Pune', 'Teju'], 'Ashu']
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# [13, 11, 1, 2, 20, 17]
# [13, 11, 1, 20, 17]
# Unsorted list : [1, 2, 3, 4, 5, 3, 2, 3, 4, 5, 6, 5, 4, 6, 7, 8, 9, 0, 7, 6, 5, 4, 6, 7, 7, 9]
# Sorted list : [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9]
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Sum of list  is : 128
# ASCII : : [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9]
#
# Process finished with exit code 0
