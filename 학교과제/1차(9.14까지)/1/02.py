import random
today = random.randint(0, 6)
print(today)
if today == 0:
	print(2)
elif today == 1:
	print(3)
elif today == 2:
	print(4)
elif today == 3:
    print(5)
elif today == 4:
    print(6)
elif today == 5:
    print(0)
else:
    print(1)