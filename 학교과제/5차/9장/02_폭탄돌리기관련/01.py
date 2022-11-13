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
    
import random
  
def hot_potato(name_list):

    sim_queue = Queue()
    
    # 큐에 사람 목록 추가
    for name in name_list:
        sim_queue.enqueue(name)

    # 게임 진행
    while sim_queue.size() > 1:
        num = random.randint(1, 100)
        # num 번 폭탄 돌린 후 탈락자 지정
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()

    return sim_queue.dequeue()    # 마지막 남은 사람

print(hot_potato(["형택", "진서", "은혜", "민규", "정은", "청용"]))