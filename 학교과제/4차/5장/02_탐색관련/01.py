#길이가  𝑛 인 리스트에 포함된 항목들의 최솟값을 구하는 두 개의 함수를 구현하라.
#방법 1: 각 항목을 다른 모든 항목과 비교. 일정 시간복잡도는  𝑇(𝑛)∈𝑂(𝑛2) .
#방법 2:  𝑇(𝑛)∈𝑂(𝑛) , 즉, 선형 시간복잡도를 갖도록 구현할 것.
#참고: https://www.youtube.com/watch?v=p0COF_m6H1c
#방법1
def find_min1(list_min):
    min = list_min[0]
    for i in list_min:
        flag = 1
        for j in list_min:
            if i > j:
                flag = 0
        if flag == 1:
            min = i
    return min
            

#방법2
def find_min2(list_min):
    min = list_min[0]
    n = len(list_min)
    for i in range(1, n):
        if(min > list_min[i]):
            min = list_min[i]
    return min