import sys

def dfs(len, idx):
    if len == l:
        gather = 0			#모음
        consonant = 0		#자음
        
        for i in range(l):
            if arr[i] in 'aeiou': 
                gather += 1
            else: 
                consonant += 1
                
        if gather >= 1 and consonant >= 2:
            print(''.join(arr))
        return
    
    for i in range(idx, c):
        if check[i] == 0:
            arr.append(s[i])
            check[i] = 1
            dfs(len + 1, i + 1)
            check[i] = 0
            del arr[-1]
            
l, c = map(int, sys.stdin.readline().split())
check = [0 for _ in range(c)]
arr = []
s = sys.stdin.readline().split()
s.sort()
dfs(0, 0)