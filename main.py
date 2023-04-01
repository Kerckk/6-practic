def sizer(cls):
    class SizedClass(cls):
        @property
        def size(self):
            if hasattr(self, '__len__'):
                return len(self)
            elif hasattr(self, '__abs__'):
                return abs(self)
            else:
                return 0
    return SizedClass

@sizer
class MyClass:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

@sizer
class MyClass2:
    def __init__(self, data):
        self.data = data

    def __abs__(self):
        return abs(self.data)

@sizer
class MyClass1:
    def __init__(self, data):
        self.data = data


a = MyClass([1, 2, 3, 4, 5])
print(a.size)  # 5

b = MyClass2(-10)
print(b.size)  # 10

c = MyClass1({'a': 1, 'b': 2, 'c': 3})
print(c.size)  # 0