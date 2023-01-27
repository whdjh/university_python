#재귀를 사용하지 않으면서 quick_sort() 함수를 구현한 후에 제대로 작동함을 확인하라.
#참고 : https://www.geeksforgeeks.org/iterative-quick-sort/

def partition(a_list, left, right):
    i = (left - 1)
    x = a_list[right]

    for j in range(left, right):
        if   a_list[j] <= x:
            #작은 인덱스부터 늘려나감
            i = i + 1
            a_list[i], a_list[j] = a_list[j], a_list[i]
    a_list[i + 1], a_list[right] = a_list[right], a_list[i + 1]
    
    return (i + 1)
 
# left는 시작 인덱스 right는 마지막 인덱스
def quickSortIterative(a_list, left, right):
    size = right - left + 1
    result = [0] * (size)
    top = -1
 
    #처음과 끝값을 리스트에 넣는다.
    top = top + 1
    result[top] = left
    top = top + 1
    result[top] = right
 
    #빈 리스트이 아닐때까지 뺴낸다.
    while top >= 0:
        #끝과 처음을 뺀다.
        right = result[top]
        top = top - 1
        left = result[top]
        top = top - 1
        #정렬된 배열의 올바른 위치에 피벗 요소 설정
        p = partition( a_list, left, right )
        #피벗의 왼쪽에 요소가 있는 경우, 왼쪽의 결과를 넣는다.
        if p - 1 > left:
            top = top + 1
            result[top] = left
            top = top + 1
            result[top] = p - 1
        #피벗의 오른쪽에 요소가 있는 경우, 오른쪽의 결과를 넣는다.
        if p + 1 < right:
            top = top + 1
            result[top] = p + 1
            top = top + 1
            result[top] = right
            
a_list = [4, 3, 5, 2, 1, 3, 2, 3]
n = len(a_list)
quickSortIterative(a_list, 0, n - 1)
print (a_list)