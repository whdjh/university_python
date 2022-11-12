class Stack:
    """리스트를 활용한 스택 구현"""

    def __init__(self):
        """새로운 스택 생성"""
        self._items = []

    def __repr__(self):
        """스택 표기법: <[1, 2, 3]> 등등"""
        return f"<{self._items}>"
        
    def is_empty(self):
        """비었는지 여부 확인"""
        return not bool(self._items)

    def push(self, item):
        """새 항목 추가"""
        self._items.append(item)

    def pop(self):
        """항목 제거"""
        return self._items.pop()

    def peek(self):
        """탑 항목 반환"""
        return self._items[-1]

    def size(self):
        """항목 개수 반환"""
        return len(self._items)
    
prec = {}
prec["*"] = 3
prec["/"] = 3
prec["+"] = 2
prec["-"] = 2
prec["("] = 1

def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
    
def infix_eval(infix_expr):
    op_stack = Stack()
    operand_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token not in '()*/+-**':
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
        
    for token in postfix_list:
        if token not in '*/+-':
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)

    return operand_stack.pop()