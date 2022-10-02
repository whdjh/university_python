import random

n = random.randint(1, 99)

print(n)

def terminalZeroCount(n):
    
    two = 0
    five = 0

    for n in range(1, n + 1):
        while n % 2 == 0:
            two += 1
            n //= 2

        while n % 5 == 0:
            five += 1
            n //= 5

    return min(two, five)

print(terminalZeroCount(n))