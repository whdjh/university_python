#직접구현
'''n = list(input())
cnt, num = 1, 1
sum = 0
res = ''
arr = []

# 슬라이싱을 통한 역순
for i in n[::-1]:
    arr.append(i)

for i in range(len(arr)):
    sum += (int(arr[i]) * num)
    num *= 2
    cnt += 1
    if cnt > 3 or i == len(arr) - 1:
        res += str(sum)
        sum = 0
        cnt, num = 1, 1

print(''.join(reversed(res)))'''

#내장함수사용
print(oct(int(input(), 2))[2:])