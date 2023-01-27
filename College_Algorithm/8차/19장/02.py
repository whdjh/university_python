'''def edit_distance(s, t):
    m = len(s) + 1
    n = len(t) + 1
    D = [[0] * m for _ in range(n)]
    D[0][0] = 0
    
    for i in range(1, m):
        D[0][i] = D[0][i - 1] + 20
    
    for j in range(1, n):
        D[j][0] = D[j - 1][0] + 20
    
    
    for i in range(1, n):
        for j in range(1, m):
            cost = 5

            if s[j - 1] != t[i - 1]:
                cost = 40
            #삭제, 삽입, 교체(삭제후 삽입이라고 가정)
            D[i][j] = min(D[i][j - 1] + 20, D[i - 1][j] + 20, D[i - 1][j - 1] + cost)
            
    
    return D[-1][-1]
 
print(edit_distance("algorithm", "alligator")) '''


def edit_distance_lcs(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)

    #이중배열을 생성한다.
    double_list = [[0] * (str2_len + 1) for _ in range(str1_len + 1)]

    #같은 문자를 찾는 반복문. 유지할 문자의 갯수를 찾는다.
    for i in range(1, str1_len+1):
        for j in range(1, str2_len+1):
            if str1[i-1] == str2[j-1]:
                double_list[i][j] = double_list[i-1][j-1] + 1
            else:
                double_list[i][j] = max(double_list[i][j-1], double_list[i-1][j])
                
    m = len(str1) - double_list[-1][-1]
    n = len(str2) - double_list[-1][-1]
    
    #유지 하기위한 값
    maintain_cost = double_list[-1][-1] * 5
    
    #삽입을 할지, 삭제를 할지 정한다.
    #str1이 더 길다. n만큼은 삭제 후 삽입을 시켜야하고 m - n만큼은 삭제만 시켜주면된다.
    if m > n:
        result = maintain_cost + n * (20 + 20) + (m - n) * 20
    #str2가 더 길다. m만큼은 삭제 후 삽입을 시켜야하고 n - m만큼은 추가만 시켜주면된다.
    elif m < n:
        result = maintain_cost + m * (20 + 20) + (n - m) * 20
    #str1의 길이와 str2의 길이가 같다. m(or n)만큼 삭제후 삽입을 해줘야한다.
    else:
        result = (m * 40) + maintain_cost
    
    return result
                
print(edit_distance_lcs("algorithm", "alligator"))    