import sys
input = sys.stdin.readline	#출력시간 줄이기 위해

n = int(input())	#명령의 수
stack = []

def push(x):
    stack.append(x)
    
def pop():
    if(len(stack) == 0):
        print (-1)
    else:
        print (stack.pop())
    
def size():
    print (len(stack))

def empty():
    if(len(stack) == 0): 
        print(1)
    else: 
        print(0)
def top():
    if(len(stack) == 0):
        print(-1)
    else:
        print(stack[-1])
        
for i in range(n):
    stackorder = input().split()
    if(stackorder[0] == 'push'):
        push(stackorder
[1])
    if(stackorder[0] == 'pop'):
        pop()
    if(stackorder[0] == 'size'):
        size()
    if(stackorder[0] == 'empty'):
        empty()
    if(stackorder[0] == 'top'):
        top()