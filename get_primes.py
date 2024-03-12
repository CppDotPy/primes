def get_primes(start, end):

    building_blocks = [2, 3, 5, 7, 9]
    primes = []

    for n in range(start, end + 1):

        is_prime = True
        for i in building_blocks:
            if n % i == 0: is_prime = False
        if n in building_blocks: is_prime = True
        if is_prime: primes.append(n)

    return primes

