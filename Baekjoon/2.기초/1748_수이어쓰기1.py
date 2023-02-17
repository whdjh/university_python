n = input()
len_n = len(n) - 1
cnt = 0

for i in range(len_n):
    cnt += 9 * (10 ** i) * (i + 1)		#각 자릿수를 곱하면 되는 규칙 찾기
    i += 1

cnt += ((int(n) - (10 ** len_n)) + 1) * (len_n + 1)

print(cnt)