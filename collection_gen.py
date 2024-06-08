squares = [x * x for x in range(10)]
print(squares)

unique_squares = {x * x for x in range(10)}
print(unique_squares)

names = ["Alice", "Bob", "Charlie", "Diana"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)
