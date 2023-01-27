#재귀를 사용하지 않으면서 mergesort() 함수를 구현한 후에 제대로 작동함을 확인하라.
#참고 : https://www.geeksforgeeks.org/iterative-merge-sort/

def mergesort(a_list):
    width = 1   
    n = len(a_list)                                         

    while (width < n):
        left = 0;
        while (left < n):
            right = min(left + (width * 2 - 1), n - 1)        
            mid = min(left + width - 1, n - 1)      
            merge(a_list, left, mid, right)
            left += width * 2
        width *= 2
    return a_list
   
#병합하는 기능
def merge(a_list, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    Left = [0] * n1
    Right = [0] * n2
    
    for i in range(0, n1):
        Left[i] = a_list[left + i]
    for i in range(0, n2):
        Right[i] = a_list[mid + i + 1]

    i = 0
    j = 0
    k = left
    
    while i < n1 and j < n2:
        if Left[i] <= Right[j]:
            a_list[k] = Left[i]
            i += 1
        else:
            a_list[k] = Right[j]
            j += 1
        k += 1
 
    while i < n1:
        a_list[k] = Left[i]
        i += 1
        k += 1
 
    while j < n2:
        a_list[k] = Right[j]
        j += 1
        k += 1
        
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

mergesort(a_list)
 
print(a_list)