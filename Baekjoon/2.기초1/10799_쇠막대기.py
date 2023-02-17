razer = list(input())
ans = 0
stack = []

for i in range(len(razer)):
    if razer[i] == '(':
        stack.append('(')

    else:
        if razer[i-1] == '(': 
            stack.pop()
            ans += len(stack)

        else:
            stack.pop() 
            ans += 1 

print(ans)