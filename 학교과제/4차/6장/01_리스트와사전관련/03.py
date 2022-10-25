from timeit import Timer

def dict_del():
    Dict_a = {i: '0' for i in range(100)}
    del Dict_a[1]

def list_del():
    list_a = [i for i in range(100)]
    del list_a[1]

t1 = Timer("dict_del()", "from __main__ import dict_del")
print(f"dict_del() 메서드:\t {t1.timeit(number=1000_000):.3f} 초")

t2 = Timer("list_del()", "from __main__ import list_del")
print(f"list_del() 메서드:\t {t1.timeit(number=1000_000):.3f} 초")