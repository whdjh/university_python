n = 1000_000

x = {j: 0 for j in range(n)}

def find_val_first():
    return x[0]

def find_val_middle():
    return x[n // 2]

def find_val_last():
    return x[n - 1]

def change_first():
    x[0] = 1
    return

def change_middle():
    x[n // 2] = 1
    return

def change_last():
    x[n - 1] = 1
    return

from timeit import Timer

t1 = Timer("find_val_first()", "from __main__ import find_val_first")
print(f"find_val_first() 메서드:\t {t1.timeit(number=1000_000):.3f} 초")
t2 = Timer("find_val_middle()", "from __main__ import find_val_middle")
print(f"find_val_middle() 메서드:\t {t2.timeit(number=1000_000):.3f} 초")
t3 = Timer("find_val_last()", "from __main__ import find_val_last")
print(f"find_val_last() 메소드:\t {t3.timeit(number=1000_000):.3f} 초")
t4 = Timer("find_val_first()", "from __main__ import find_val_first")
print(f"find_val_first() 메서드:\t {t4.timeit(number=1000_000):.3f} 초")
t5 = Timer("find_val_middle()", "from __main__ import find_val_middle")
print(f"find_val_middle() 메서드:\t {t5.timeit(number=1000_000):.3f} 초")
t6 = Timer("find_val_last()", "from __main__ import find_val_last")
print(f"find_val_last() 메소드:\t {t6.timeit(number=1000_000):.3f} 초")