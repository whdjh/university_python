class Stack:
    def __init__(self):
        self._items = []

    def __repr__(self):
        return f"<{self._items}>"
        
    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)

def rev_string(my_str):
    s_str = Stack()								#스택생성
    reverse_str = ''							#리버스된값들로 저장하기위한 변수
    #my_str의 문자열을 s_str로 넣어줌
    for i in my_str:
        s_str.push(i)
    #reverse_str에 s_str요소 하나씩 뺴서 기존 reverse_str과 함께 넣어줌
    for i in range(s_str.size()):
        reverse_str += s_str.pop()
    return reverse_str

assert rev_string('honey') == 'yenoh'
assert rev_string('hello world3') == '3dlrow olleh'