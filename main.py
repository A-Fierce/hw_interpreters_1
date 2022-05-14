class FlatIterator:
    def __init__(self, n_list):
        new_list = []
        for item in nested_list:
            if type(item) == list:
                new_list += item
            else:
                new_list.append(item)
        self.n_list = new_list
        self.start = -1
        self.end = len(new_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.n_list[self.start]


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)