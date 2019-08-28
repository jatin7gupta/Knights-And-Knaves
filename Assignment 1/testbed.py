def recursive_fibonacci(n):
    if n >= 2:
        return recursive_fibonacci(n - 2) + recursive_fibonacci(n - 1)
    return n


print(recursive_fibonacci(10))