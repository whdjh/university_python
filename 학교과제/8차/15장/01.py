#정수들의 리스트를 이용하여 순차탐색과 이진탐색의 성능을 비교하는 모의실험을 구현하라.

#우선 들어가기에 앞서 이진탐색은 오름차순으로 정렬되어있는 정수들의 리스트 중 항목을 찾을때 사용하므로 
#순차탐색도 오름차순으로 정렬되어있는 정수를 찾을때 사용하는 코드를 사용하기로 한다.

#순차탐색
def ordered_sequential_search(a_list, item):
    pos = 0
    
    while pos < len(a_list):
        if a_list[pos] == item:
            return True
        else:
            if a_list[pos] > item:   # 항목이 찾는 값보다 큰 경우 바로 종료
                return False
            else:
                pos = pos + 1
    return False

#이진탐색
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

a_list = [ 17, 28, 43, 67, 88, 92, 100 ]
item = 43

print(ordered_sequential_search(a_list, item))
print(binary_search(a_list, item))

from time import time
start= time()
ordered_sequential_search(a_list,item)
end = time()
 
start1 = time()
binary_search(a_list,item)
end1 = time()


sequential = end - start
binary = end1 - start1
count1 = 0
count2 = 0
for i in range(100):
  count1 += sequential
  count2 += binary

print(f"순차탐색평균: {count1 / i : .6f} \n이진탐색평균: {count2 / i : .6f}")