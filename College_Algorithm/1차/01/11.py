import random

weight = random.randint(0, 99)

print(weight)

if weight < 5:
    print('5,000원')

elif weight < 10:
    print('8,000원')
    
else:
    print('10,000원')