n = 1000_000

s = [x for x in range(n)] #리스트 생성

def find_first():
    return s[0]	#첫번째 요소 출력

def find_middle():
    return s[n // 2] #중간인덱스 요소 출력

def find_last():
    return s[n - 1] #마지막 요소 출력

from timeit import Timer

t1 = Timer("find_first()", "from __main__ import find_first")
print(f"index_first() 메서드:\t {t1.timeit(number=1000_000):.3f} 초")
t2 = Timer("find_middle()", "from __main__ import find_middle")
print(f"index_middle() 메서드:\t {t2.timeit(number=1000_000):.3f} 초")
t3 = Timer("find_last()", "from __main__ import find_last")
print(f"index_last() 메소드:\t {t3.timeit(number=1000_000):.3f} 초")