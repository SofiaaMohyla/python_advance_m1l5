class CustomList:
    def __init__(self, elements):
        self.elements = elements

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.elements):
            result = self.elements[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


# Використання кастомного списку
custom_list = CustomList([1, 2, 3, 4, 5])

my_iter = iter(custom_list)
print(next(my_iter))
print(next(my_iter))
