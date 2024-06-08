even_squares_gen = (x * x for x in range(10) if x % 2 == 0)

for square in even_squares_gen:
    print(square)
