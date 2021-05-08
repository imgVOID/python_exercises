def prime_checker():
    while True:
        num = yield
        if num % 2:
            for x in range(3, int(num ** 0.5 + 1), 2):
                if not num % x:
                    break
            else:
                yield num
