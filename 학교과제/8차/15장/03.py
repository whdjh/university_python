#슬라이싱을 사용하지 않는 재귀 이진탐색 알고리즘을 사용하는 함수를 구현하라.

def binarySearch_Recursive(a_list, left, right, item):
    # 탐색 구간: 전체 리스트
    if left > right:
        return False
    
    mid = (left + right) // 2	#탐색 구간의 중앙위치
 
    #항목을 찾은 경우
    if item == a_list[mid]:
        return True
    
    # 항목을 아직 찾지 못한 경우
    elif item < a_list[mid]: 	#중앙위치 왼편으로 탐색구간 조정
        return binarySearch_Recursive(a_list, left, mid - 1, item)

    else:	# 중앙위치 오른편으로 탐색구간 조정	
        return binarySearch_Recursive(a_list, mid + 1, right, item)