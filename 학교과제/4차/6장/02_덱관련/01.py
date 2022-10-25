from collections import deque
from timeit import Timer

def rotate(k):
    q = deque([x for x in range(100)])
    q.rotate(k)
  
t1 = Timer("rotate(-1)", "from __main__ import rotate")
print(f"rotate k = -1 :\t {t1.timeit(number=1000):.3f} 초")
t2 = Timer("rotate(-4)", "from __main__ import rotate")
print(f"rotate k = -4 :\t {t2.timeit(number=1000):.3f} 초")
t3 = Timer("rotate(1)", "from __main__ import rotate")
print(f"rotate k = 1 :\t {t3.timeit(number=1000):.3f} 초")
t4 = Timer("rotate(8)", "from __main__ import rotate")
print(f"rotate k = 8 :\t {t4.timeit(number=1000):.3f} 초")