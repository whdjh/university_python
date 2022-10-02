a, b = map(int, input().split()) # 두 개의 수는 가운데에 공백을 포함한 하나의 문자열로 입력받게 된다. 
								 #이 문자열을 input 함수로 입력받고 split 함수로 나눌 때 
         						 #괄호에 아무것도 입력하지 않으면 공백을 기준으로 문자를 나눌 수 있다.
                				 #그리고 map 함수를 이용해서 split 함수로 나눈 두 개의 문자를 
                     			 #int타입인 정수로 변환시켜 준다.
if a > b:
    print('>')

elif a < b:
    print('<')

else:
    print('==')