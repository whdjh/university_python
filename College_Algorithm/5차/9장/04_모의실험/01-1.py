class Queue:
    """리스트를 활용한 큐 구현"""

    def __init__(self):
        """새로운 큐 생성"""
        self._items = []
    
    def __repr__(self):
        """큐 표기법: <<[1, 2, 3]>> 등등"""
        return f"<<{self._items}>>"
    
    def is_empty(self):
        """비었는지 여부 확인"""
        return not bool(self._items)

    def enqueue(self, item):
        """꼬리에 항목 추가"""
        self._items.insert(0, item)

    def dequeue(self):
        """머리 항목 삭제"""
        return self._items.pop()

    def size(self):
        """항목 개수 확인"""
        return len(self._items)

n = 3	#주차공간수
m = 4	#오늘 주차할 차량 갯수

fee = [] * n		#주차요금
weight = []	* m		#무게
wait = Queue()		#기다림
use = [0] * n		#주차 공간 할당
total = 0

fee = [int(input(f"{i + 1}번째 주차공간의 요금은 얼마인가요?")) for i in range(n)]
weight = [int(input(f"{i + 1}번째 차량의 무게는 몇키로인가요?")) for i in range(m)]
 
for i in range(m * 2):
    car = int(input(f"양수면 입차 음수면 출차입니다. 범위는 {-n}에서 {n}까지 입력하세요"))
    if car > 0:
        print(f"{car}번째로 입차합니다")
        if 0 in use:
            for j in range(n):
                if use[j] == 0:
                    use[j] = [car]
                    break 
        else:
            wait.enqueue(car)
    else:
        if(car == 0):
            print("오류")
            break
        print(f"{-car}번째는 출차됩니다. 따라서 {-car}번째는 비어있습니다.")
        use[-car-1] = 0
        total += weight[-car - 1] * fee[-car-1]
        if wait != 0:
            use[-car] = wait.dequeue()
print(f"오늘 자동차 수입은 {total} 입니다.")