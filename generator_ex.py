def fib(limit=100):
    x, y = 0, 1
    yield x
    yield y
    counter = 2

    while counter < limit:
        x, y = y, x + y
        yield y
        counter += 1


if __name__ == '__main__':
    fib_numbers = fib(20)
    for i in range(5):
        print(next(fib_numbers))

    for i in range(10):
        print(next(fib_numbers))

    print("wow", next(fib_numbers))

    for i in fib_numbers:
        print(i)
