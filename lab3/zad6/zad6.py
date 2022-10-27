def prime(n: int, i: int) -> bool:
    if i == 1:
        return True
    if n % i-1 != 0:
        return prime(n, i-1)
    return False



print(prime(4, 4))

