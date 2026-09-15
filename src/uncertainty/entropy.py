import math


def entropy(sizes):
    if not sizes or any(type(n) is not int or n <= 0 for n in sizes):
        raise ValueError("Cluster sizes must be positive integers")
    total = sum(sizes)
    return -sum((n/total) * math.log(n/total) for n in sizes)
