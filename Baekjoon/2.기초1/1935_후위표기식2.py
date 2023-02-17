n = int(input())
word = input()
num_list = [0] * n

for i in range(n):
    num_list[i] = int(input())
    
stack = []

for i in word:
    if 'A' <= i <= 'Z':
        stack.append(num_list[ord(i) - ord('A')]) 	#ord(), 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
    else:
        str2 = stack.pop()
        str1 = stack.pop()
        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)

print('%.2f' %stack[0])