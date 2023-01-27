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
        """머리에 항목 추가"""
        self._items.append(item)

    def dequeue(self):
        """꼬리 항목 삭제"""
        return self._items.pop(0)

    def size(self):
        """항목 개수 확인"""
        return len(self._items)