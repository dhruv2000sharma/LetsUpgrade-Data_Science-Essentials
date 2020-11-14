# Name : DHRUV SHARMA
# Assignment No : 2(Que 3)

# Questions 3:
# You have seen in the videos how powerful dictionary data structure is.
# In this assignment, given a number n, you have to write a program that generates a dictionary d which
# contains (i, i*i), where i is from 1 to n (both included).
# Then you have to just print this dictionary d.
# Example:
# Input: 4
# will give output as
# {1: 1, 2: 4, 3: 9, 4: 16}
# Input Format:
# Take the number n in a single line.
# Output Format:
# Print the dictionary d in a single line.
# Example:
# Input:
# 8
# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

my_dictionary = {}
n = int(input())
my_dictionary = dict()

for i in range(1, n+1): # star and end value
    my_dictionary[i] = i*i

print(my_dictionary)


# Output :
# 5
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#
# Process finished with exit code 0
