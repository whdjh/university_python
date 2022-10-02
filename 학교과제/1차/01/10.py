import random

number = random.randint(0, 99)	#분자
divisor = random.randint(0, 9)	#분모

answer = 0						#몫
print(number)
print(divisor)

while(number > divisor):
	number = number - divisor
	answer = answer + 1

print(number)
print(answer)