# Name : DHRUV SHARMA
# Assignment no : 2(Que 1)

# Questions 1:
# Create an empty list. Accept 10 numbers from the user and append to it the list if it is an even number.

my_list = []
# print(my_list)
for i in range(10):
    i = int(input())
    if (i % 2) == 0:
        my_list.append(i)
    else:
        continue

print(my_list)

# Output 1:
# []
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# 100
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# Process finished with exit code 0

# Output 2 :
# []
# 10
# 17
# 21
# 20
# 30
# 14
# 41
# 71
# 57
# 92
# [10, 20, 30, 14, 92]
#
# Process finished with exit code 0

# Output 3:
#
# []
# 13
# 11
# 21
# 31
# 41
# 51
# 57
# 97
# 87
# 77
# []
#
# Process finished with exit code 0
