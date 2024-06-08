

a = [1, 2, 3, 4]
b = [element*2 for element in a]
print(sum(b))


a = [1, 2, 3, 4]
b = [element for element in a if element % 2 == 0]
print(sum(b))