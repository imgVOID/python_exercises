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
