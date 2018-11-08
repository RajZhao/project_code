class singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(singleton):
    a = 1


one = MyClass()
one.a = 3
two = MyClass()
# print(one == two)
# print(id(one))
# print(id(two))
print(two.a)
