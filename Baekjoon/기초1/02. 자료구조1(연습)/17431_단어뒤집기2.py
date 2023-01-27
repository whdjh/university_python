import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":       
        i += 1 
        while word[i] != ">":     
            i += 1 
        i += 1               
    elif word[i].isalnum():  #문자열이 알파벳과 숫자로만 구성되었는지 확인하는 메소드
        start = i
        while i < len(word) and word[i].isalnum():
            i+=1
        tmp = word[start:i] 
        tmp.reverse()      
        word[start:i] = tmp
    else:                 
        i += 1                

print("".join(word))