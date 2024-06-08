def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# Використання генераторної функції
for number in even_numbers(10):
    print(number)
