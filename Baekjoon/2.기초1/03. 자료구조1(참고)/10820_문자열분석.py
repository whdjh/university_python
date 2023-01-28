import sys

while True:
    str = sys.stdin.readline().rstrip('\n')		#줄바꿈을 무시하기위해 사용!
    if not str:
        break

    #차례대로 소문자, 대문자, 숫자, 공백
    low, upper, digit, space = 0, 0, 0, 0
    for i in str:
        if i.islower():
            low += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            digit += 1
        elif i.isspace():
            space += 1

    print(low, upper, digit, space)