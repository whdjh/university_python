'''x = input("문자열을 입력하시오 :")

print("대문자, 소문자, 숫자, 특수문자의 개수")

count1 = 0 
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for i in x:
    if 'A' <= i <= 'Z':
        count1 += 1
    elif "a" <= i <= "z":
        count2 += 1
    elif "1" <= i <= "9":
        count3 += 1
    else:
        count4 += 1
print(f"대문자 = {count1}\n소문자 = {count2}\n숫자 = {count3}\n특수문자 = {count4}")'''

import re
p = re.compile('cde')

m = p.match("ABcde9876@")
print(m)