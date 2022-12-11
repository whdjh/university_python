def edit_distance(s, t):
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
 
print(edit_distance("algorithm", "alligator")) 
