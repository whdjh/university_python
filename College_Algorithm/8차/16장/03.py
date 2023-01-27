#정수 500개를 무작위로 생성한 후 소개된 네 개의 정렬 알고리즘의 실행시간을 평가하는 모의실험을 수행하라.

#버블
def bubble_sort_short(a_list):
    
    for i in range(len(a_list) - 1, 0, -1):
        exchanges = False    # 패스 기간 내 자리교환 발생 여부 저장
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                exchanges = True
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]

        if not exchanges:   # 패스 기간 동안 자리교환이 발생하지 않은 경우 조기종료
            print("조기종료!")
            break
        
#선택
def selection_sort(a_list):
    for i in range(len(a_list)-1, 0, -1):
        max_idx = 0
        for j in range(i):
            if a_list[j] > a_list[max_idx]:
                max_idx = j
        
        a_list[max_idx], a_list[i] = a_list[i], a_list[max_idx]
        
#합병
def merge_sort(a_list):
    # 분할 과정
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        
        # 합병 과정
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
            
#퀵
def partition(a_list, first, last):
    pivot_val = a_list[first]   # 피벗
    left_mark = first + 1       # 탐색 구간 시작
    right_mark = last           # 탐색 구간 끝
    done = False                # 탐색 종료여부 확인

    while not done:
        while left_mark <= right_mark and a_list[left_mark] < pivot_val:
            left_mark = left_mark + 1
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            right_mark = right_mark - 1
        
        # 자리 교환
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]
            
    # 피벗 자리 교환
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    # 피벗 위치 반환
    return right_mark
  
# 재귀 보조함수: 리스트의 지정된 구간에 대해 partion() 함수 재귀적으로 활용
def quick_sort_helper(a_list, first, last):
    if first < last:
        split = partition(a_list, first, last)

        quick_sort_helper(a_list, first, split - 1)
        quick_sort_helper(a_list, split + 1, last)

# 재귀 함수
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)
    
import random
a_list = []

for _ in range(501):
  a = random.randint(1, 501)
  a_list.append(a)
  
from time import time
start= time()
bubble_sort_short(a_list)
end = time()
 
start1 = time()
selection_sort(a_list)
end1 = time()

start2 = time()
merge_sort(a_list)
end2 = time()

start3 = time()
quick_sort(a_list)
end3 = time()

bubble = end - start
selection = end1 - start1
merge = end2 - start2
quick = end3 - start3


print(f"버블정렬시간: {bubble : .6f} \n선택정렬시간: {selection : .6f} \n합병정렬시간: {merge : .6f} \n퀵정렬시간: {quick : .6f}")