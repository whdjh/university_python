#반복을 사용하는 이진탐색과 재귀 이진탐색 알고리즘의 성능을 비교하는 모의실험을 구현하라. 
#성능차이가 발생한다면 그 이유를 설명하라.

#반복을 사용하는 이진탐색
def binary_search(a_list, item):
    # 탐색 구간: 전체 리스트
    first = 0
    last = len(a_list) - 1

    # 탐색 구간의 크기가 0이상인 경우 반복
    while first <= last:
        # 탐색 구간의 중앙위치
        midpoint = (first + last) // 2
        
        if a_list[midpoint] == item:   # 항목을 찾은 경우
            return True
        # 항목을 아직 찾지 못한 경우
        elif item < a_list[midpoint]:  # 중앙위치 왼편으로 탐색구간 조정
            last = midpoint - 1
        else:                          # 중앙위치 오른편으로 탐색구간 조정
            first = midpoint + 1
    return False

#재귀를 사용하는 이진탐색
def binary_search_rec(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        
        # 재귀호출: 탐색구간 조정
        elif item < a_list[midpoint]:
            return binary_search_rec(a_list[:midpoint], item)
        else:
            return binary_search_rec(a_list[midpoint + 1 :], item)
    
a_list = [ 17, 28, 43, 67, 88, 92, 100 ]
item = 43
left = 0
right = len(a_list)

print(binary_search_rec(a_list, item))
print(binary_search(a_list, item))

from time import time
start= time()
binary_search_rec(a_list, item)
end = time()
 
start1 = time()
binary_search(a_list,item)
end1 = time()


binary_recursive = end - start
binary = end1 - start1

count1 = 0
count2 = 0
for i in range(100):
  count1 += binary_recursive
  count2 += binary

print(f"재귀이진탐색평균: {count1 / i : .6f} \n반복이진탐색평균: {count2 / i : .6f}")

#재귀함수를 호출하는데 있어 스택 오버헤드가 크기때문에 성능차이가 반복문과 재귀함수의 차이가 나타난다.
#오버헤드가 크다는 것은 재귀함수는 호출시마다 쓰레드가 생성되어 처리함으로써
#기존 반복문에 비해 부하가 생기는 경우를 말한다고 한다. 
#그러고 수업내용을 참고하자면 재귀호출될 때마다 새로운 리스트를 슬라이싱으로 생성하여 사용하기 때문에
#슬라이싱에 필요한 시간이 추가로 요구한다.