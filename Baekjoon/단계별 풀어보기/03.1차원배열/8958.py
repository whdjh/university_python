n = int(input())

for i in range(n):
    new_num = 0
    total = 0
    ox = input()
    for x in ox:
        if x == 'O':
            new_num += 1
            
        elif x == 'X':
            new_num = 0
        
        total += new_num
    print(total)