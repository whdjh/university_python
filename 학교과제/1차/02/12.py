def int_clone(a, n):
    assert n > 0
    x = list(range(a, a * n + 1, a))
    return x

print(int_clone(2, 3))