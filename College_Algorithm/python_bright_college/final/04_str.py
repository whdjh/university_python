#파이썬은 정규 표현식을 지원하기 위해 re모듈을 제공한다.
import re
 
str = input("문자열을 입력하시오 :")	#문자열입력하는 input함수 사용

print("대문자, 소문자, 숫자, 특수문자의 개수")	#출력메세지

#[]안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위(From - To)를 의미
upper_case = re.compile('[A-Z]')		#A ~ Z중에 있는것 찾기
lower_case = re.compile('[a-z]')		#a ~ z중에 있는것 찾기
num_case = re.compile('[0-9]')			#0 ~ 9중에 있는것 찾기
etc_case = re.compile('[^0-9a-zA-Z]')   #^는 제외한다는 의미, 숫자, 대문자, 소문자 제외하고 찾기. 즉, 특수문자!

#findall()메소드는 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다.
upper = upper_case.findall(f"{str}")	#upper_case에 해당하는 것들 리턴
lower = lower_case.findall(f"{str}")	#lower_case에 해당하는 것들 리턴
num = num_case.findall(f"{str}")		#num_case에 해당하는 것들 리턴
etc = etc_case.findall(f"{str}")		#etc_case에 해당하는 것들 리턴

print(f"대문자 = {len(upper)}\n소문자 = {len(lower)}\n숫자 = {len(num)}\n특수문자 = {len(etc)}")    #\n은 이스케이프, len()함수는 리스트길이를 의미하고 그래서 그 길이를 출력하면 총 갯수가 나온다