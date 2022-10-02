n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i), end="") #print 끝에 end=""를 더해 print의 기본 설정인 개행을 막아줍니다.
								#(Python은 end 뒤에 따로 설정을 해주지 않으면 자동으로 개행을 해줍니다.)
    print('*' * i)