# Lists

number = [0, 1, 3, 4, 5]
print(number[0])
number[0] = 4
print(number)
print('-------' * 30)

# 2D Lists
# Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])
print('-------' * 30)
print(matrix[0][1])
print('-------' * 30)

for row in matrix:
    for columns in row:
        print(columns)
print('-------' * 30)


# List Methods
prices = [3, 5, 6, 6, 0]
prices.append(8)
print(prices)
prices.insert(0, 10)
print(prices)
prices.remove(0)
print(prices)
# remove the last item on the list
prices.pop()
print(prices)
# check the item's index
print(prices.index(3))
prices.sort()
print(prices)
prices.reverse()
print(prices)






