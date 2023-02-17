n = int(input())
lion = [[0] * 3 for _ in range(100001)]

for i in range(3):
    lion[1][i] = 1
    
for i in range(2, 100001):
    lion[i][0] = lion[i - 1][1] + lion[i - 1][2] % 9901
    lion[i][1] = lion[i - 1][0] + lion[i - 1][2] % 9901
    lion[i][2] = lion[i - 1][0] + lion[i - 1][1] + lion[i - 1][2] % 9901
print(sum(lion[n]) % 9901)