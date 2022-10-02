import  random

n = random.randint(1, 99)

print(n)

sum = 0

for i in range(1, n + 1):
    if n % i == 0:
        sum = sum + i      
print(sum)