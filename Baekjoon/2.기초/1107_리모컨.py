import sys

n = int(sys.stdin.readline())								#원하는 채널
m = int(sys.stdin.readline())								#고장난숫자갯수
error_num = list(map(int, sys.stdin.readline().split()))	#고장난숫자
min_cnt = abs(100 - n)

for i in range(1000001):
    i = str(i)
    
    for j in range(len(i)):
        if int(i[j]) in error_num:	#고장확인
            break
        elif j == len(i) - 1:		#고장난 숫자가 없다면
            min_cnt = min(min_cnt, abs(int(i) - n) + len(i))	#abs는 절댓값
            
print(min_cnt)