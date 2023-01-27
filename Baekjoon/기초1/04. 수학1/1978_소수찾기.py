n = int(input())
nums = map(int, input().split())
prime = 0

for i in nums:
    not_prime = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                not_prime += 1
        if not_prime == 0:
            prime += 1
            
print(prime)