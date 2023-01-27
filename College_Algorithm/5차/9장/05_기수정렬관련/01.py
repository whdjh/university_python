class Deque:
    """리스트를 활용한 덱 구현"""

    def __init__(self):
        """새로운 덱 생성"""
        self._items = []
    
    def __repr__(self):
        """덱 표기법: <~[1, 2, 3]~> 등등"""
        return f"{self._items}"
    
    def is_empty(self):
        """비었는지 여부 확인"""
        return not bool(self._items)

    def add_front(self, item):
        """머리에 항목 추가"""
        self._items.append(item)

    def add_rear(self, item):
        """꼬리에 항목 추가"""
        self._items.insert(0, item)

    def remove_front(self):
        """머리 항목 삭제"""
        return self._items.pop()

    def remove_rear(self):
        """꼬리 항목 삭제"""
        return self._items.pop(0)

    def size(self):
        """항목 개수 확인"""
        return len(self._items)

    def to_list(self):
        return self._items
    
def radix_sort(num_list):
    buckets = [Deque() for _ in range(10)]  
    num_max = max(num_list) #가장 큰수
    result = Deque()
    for num in num_list:
        result.add_front(num)
    units = 1           #자릿수(일의자리부터시작!)

    while num_max >= units:
        while result.size() != 0:
            num = result.remove_rear()
            buckets[(num // units) % 10].add_front(num)

        for bucket in buckets:
            while bucket.size() != 0:
                result.add_front(bucket.remove_rear())

        units *= 10

    return result.to_list()

num_list = [349, 12, 252, 8]

assert radix_sort(num_list) == [8, 12, 252, 349]