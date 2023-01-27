import sys

arr = [True for i in range(1000001)]

for i in range(2, 1001):
    if arr[i]:
        for j in range(i * i, 1000001, i):
            arr[j] = False
            
while True:
    n = int(sys.stdin.readline())	#한 개의 정수를 입력받을 때
    
    if n == 0:
        break
    for i in range(3, len(arr)):
        if arr[i] and arr[n - i]:
            print(f"{n} = {i} + {n - i}")
            break