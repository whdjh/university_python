import random

year = random.randint(0, 99)
month = random.randint(1, 12)
print('생년월일: {0:02d}'.format(year), end = "")
print('{0:02d}'.format(month), end = "")
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
	day = random.randint(1, 31)
	print('{0:02d}'.format(day))
 
elif month == 4 or month == 6 or month == 9 or month == 11:
    day = random.randint(1, 30)
    print('{0:02d}'.format(day))
    
else:
    day = random.randint(1, 28)
    print('{0:02d}'.format(day))

if 0 <= year <= 22:
    sex = random.randint(3, 4)
    jumin = random.randint(0, 999999)
    print('   나머지: {0:1d}'.format(sex), end = "")
    print('{0:06d}'.format(jumin))
    
if 23 <= year <= 99:
    sex = random.randint(1, 2)
    jumin = random.randint(0, 999999)
    print('   나머지: {0:1d}'.format(sex), end = "")
    print('{0:06d}'.format(jumin))