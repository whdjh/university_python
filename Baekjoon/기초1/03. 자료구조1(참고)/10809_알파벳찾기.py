s = input()

alp = list(range(97,123))  #아스키코드 숫자 범위

for i in alp:
    print(s.find(chr(i)))  #find 함수는 어떤 찾는 문자가 문자열 안에서 첫 번째에 위치한 순서를 숫자로 출력한다. 만일 찾는 문자가 문자열 안에 없는 경우에는 -1을 출력하는 함수이다.