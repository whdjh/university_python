#3번문제를 활용해서 문제를 푸는 것인가? 아님 랜덤으로 받아서 문제를 푸는것인가?#
import random
sex = random.randint(1, 4)
if sex == 1 or sex == 3:
	print('성별: {0:01d}'.format(sex), ('(남성)'))
elif sex == 2 or sex == 4:
	print('성별: {0:01d}'.format(sex), ('(여성)'))