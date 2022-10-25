#추가할 항목: 차원이 다름을 표시하기(dfs)
class TwoDArray:
    #items: 2차원 어레이 항목으로 사용될 값들. 리스트, 튜플 등 모음 자료형 사용. 저장: 리스트 활용
    def __init__(self, items):
        self.items = []
        for x in items:
            self.items.append(list(x))
        
    def __repr__(self):
        return f"myArray({self.items})"
    
    def __add__(self, other_array):
        if(len(self.items) != len(other_array.items)): #길이가 동일하지 않다!
            raise RuntimeError("길이가 달라요!")
        if(): #차원이 다르다!
            raise RuntimeError("차원이 달라요!")
        # 항목별 덧셈 실행
        return [[self_num + other_num for self_num, other_num in zip(self_list, other_list)] for self_list, other_list in zip(self.items, other_array.items)]

    def __mul__(self, other_array):
        if(len(self.items) != len(other_array.items)): #길이가 동일하지 않다!
            raise RuntimeError("길이가 달라요!")
        if(): #차원이 다르다!
            raise RuntimeError("차원이 달라요!")
        # 항목별 곱셈 실행
        return [[self_num * other_num for self_num, other_num in zip(self_list, other_list)] for self_list, other_list in zip(self.items, other_array.items)]

a = TwoDArray([[1,2], [2, 3], [3,4]])
b = TwoDArray([[10,20], [20, 30], [30,40]])

c = a + b
d = a * b

print(c)
print(d)