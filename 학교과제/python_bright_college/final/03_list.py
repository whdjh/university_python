list1 = [10, 20, 30, 40, 50]

#리스트컴프리헨션! 슬라이싱 + sum()함수를 이용해서 새로운 list2를 생성
list2 = [list1[x] if x == 0 else sum(list1[0:x+1]) for x in range(len(list1))]

print("원래 리스트:", list1)

print("새 리스트:", list2)