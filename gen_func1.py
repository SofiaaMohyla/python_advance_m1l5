def simple_generator():
    yield 1
    yield 2
    yield 3

gen_iter = simple_generator()
print(next(gen_iter))

print(next(gen_iter))