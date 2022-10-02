sum = 0

for i in range(0, 101):
	if i % 3 == 0 or i % 7 == 0:
		print(i, end = " ")
		sum = sum + i
print("")
print(f'0~100의 숫자 중 3의 배수와 7의 배수들의 합은 {sum}이다.')