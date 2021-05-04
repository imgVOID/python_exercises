def prime_checker():
    while True:
        num = yield
        if num % 2:
            for x in range(3, int(num ** 0.5 + 1), 2):
                if not num % x:
                    break
            else:
                yield num


def get_primes(checker, limit):
    yield 2
    num = 3
    count = 1
    checker.send(None)
    while count < limit:
        prime = checker.send(num)
        if prime:
            count += 1
            yield prime
        num += 1


def main():
    print([num for num in get_primes(prime_checker(), 10)])


if __name__ == '__main__':
    main()
