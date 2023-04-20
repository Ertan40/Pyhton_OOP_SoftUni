class dictionary_iter:
    def __init__(self, obj):
        self.obj = obj
        self.index = 0
        self.end = len(self.obj) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.index <= self.end:
            result = tuple
            for index, key in enumerate(self.obj.items()):
                if index == self.index:
                    result = key
            self.index += 1
            return result
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result1 = dictionary_iter({"name": "Peter", "age": 24})
for x in result1:
    print(x)