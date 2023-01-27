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
    
def tag_pairing(html_string):
    answer = True
    pair = {"<" : ">", "</" : ">"}	#태그를 쌍으로 정해줌
    s_string = []
    for i in html_string:
        if not s_string:			#s_string이 비어있다.
            if i in pair.keys():
                s_string.append(i)	#s_string에 pair의 key값을 넣어준다.
                continue
            else:					#괄호쌍이 제거되고 닫힌 괄호로 시작
                return False 
    if pair[s_string[-1]] == i:		#가장 최상단과 i와 동일할 경우	
        s_string.pop()
    elif i in pair.keys():
        s_string.append(i)
    return s_string == []

html_exp = \
"""<html>
  <head>
     <title>
        문제해결 알고리즘
     </title>
  </head>

  <body>
     <h1>스택 자료형</h1>
  </body>
</html>"""

print(tag_pairing(html_exp))