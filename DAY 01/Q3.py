# Name : DHRUV SHARMA
# Assignment :1(Que3)

# Questions 3:
# Write a program that takes cost price and selling price as input and displays whether the transaction is a
# Profit or a Loss or Neither.
# INPUT FORMAT
# The first line contains the cost price.
# The second line contains the selling price.
# OUTPUT FORMAT
# Print "Profit" if the transaction is a profit or "Loss" if it is a loss. If it is neither
# profit nor loss, print "Neither".(You must not have quotes in your output)

cost_price = int(input())
selling_price = int(input())

# print(cost_price)
# print(selling_price)

if (selling_price - cost_price) > 0:
    print("Profit")
elif (selling_price - cost_price) < 0:
    print("Loss")
else:
    print("Neither")

# Output:
# Test case 1:
# 20
# 30
# Profit
#
# Test case 2:
# 20
# 10
# Loss

# Test case 3:
# 20
# 20
# Neither

# Test case 4:
# 19
# 19
# Neither

# Test case 5:
# 23
# 7
# Loss

# Test case 5:
# 19
# 95
# Profit
