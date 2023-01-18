import sys

str1 = list(sys.stdin.readline().rstrip())	#반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않습니다.
str2 = []
n = int(sys.stdin.readline())	#sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아집니다. 또한, 변수 타입이 문자열 형태로 저장되기 때문에, 정수로 사용하기 위해서 형변환을 거쳐야 합니다.

for i in range(n):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'L':
        if str1:
            str2.append(str1.pop())
    elif cmd[0] == 'D':
        if str2:
            str1.append(str2.pop())
    elif cmd[0] == 'B':
        if str1:
            str1.pop()
    else:
        str1.append(cmd[1])
        
str1.extend(reversed(str2))
print(''.join(str1))