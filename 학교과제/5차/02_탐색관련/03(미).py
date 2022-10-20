#길이가 n인 리스트에 포함된 항목들 중에서 최댓값과 최솟값을 찾아 내는 함수를 구현하라. 
#단, 함수를 실행할 때 최대 1.5n번의 비교가 실행되어야 한다.
def find_max_min(list_maxmin):
    max = list_maxmin[0]
    min = list_maxmin[0]
    n = len(list_maxmin)
    for i in range(1, n):
        if(max < list_maxmin[i]):
            max = list_maxmin[i]
        if(min > list_maxmin[i]):
            min = list_maxmin[i]
    return max, min

v = [1, 9, 8, 100, 50]
print(find_max_min(v))