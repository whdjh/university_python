import sys
from collections import Counter
#Counter 라이브러리를 활용하여 input마다의 중복 개수를 파악한다.
#count()를 많이 사용하는 경우에는 collection 모듈인 Counter 클래스를 사용해야 유리하다.
#Counter 클래스는 딕셔너리 형태로 Key 값으로 요소의 이름, Value 값으로 요소들의 개수를 출력해준다.

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
count = Counter(num)
ans = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and count[num[stack[-1]]] < count[num[i]]:
        ans[stack.pop()] = num[i]
    stack.append(i)
    
print(*ans)