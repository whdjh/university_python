import  random

n = random.randint(1, 99)

print(n)

sum = 0

for i in range(1, n + 1):
    if '3' in str(i) or i % 3 == 0:
        sum = sum + i
        
print(sum)