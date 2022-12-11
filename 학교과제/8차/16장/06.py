#퀵정렬 알고리즘의 피벗 선택을 달리하는 알고리즘을 구현하라. 
#또한 달라진 피벗 선택이 보다 효율적으로 작동하는 경우에 대한 기준을 설명하라.
#중앙에 위치한 값 선택
#처음, 끝, 중앙에 위치한 값들의 중앙값 선택

# 분할과 정복. 피벗은 중앙 항목. 반환값은 피벗의 최종 자리 위치
def partition(a_list, first, last):
    pivot_val = a_list[(first + last) // 2]   	# 피벗
    done = False								# 탐색 종료 여부 확인

    while not done:
        while a_list[first] < pivot_val:
            first += 1
        while a_list[last] > pivot_val:
            last -= 1
        # 자리 교환
        if last < first:
            done = True
        else:
            a_list[first], a_list[last] = a_list[last], a_list[first]
            first, last = first + 1, last - 1
    
    # 피벗 위치 반환
    return first

# 재귀 보조함수: 리스트의 지정된 구간에 대해 partion() 함수 재귀적으로 활용

def quick_sort_helper(a_list, first, last):
    if first < last:
        split = partition(a_list, first, last)

        quick_sort_helper(a_list, first, split - 1)
        quick_sort_helper(a_list, split, last)
        
# 재귀 함수
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)
    
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list) 