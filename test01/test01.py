def sum():
    for i in range(10):
        yield i


m = sum()
print(next(m))
print(next(m))
print(next(m))
print(m.send(None))
