notation = list(input())
stack = []
res = ''

#우선순위는 () -> *,/ -> +,-를 생각하면서 if문 구조를 짜면 끝나는 문제
for i in notation:
    if i.isalpha():	#숫자인지 확인하는 함수
        res += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                res += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                res+= stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
            
while stack:
    res += stack.pop()
    
print(res)