#파이썬은 정규 표현식을 지원하기 위해 re모듈을 제공한다.
import re
 
str = input("문자열을 입력하시오 :")

print("대문자, 소문자, 숫자, 특수문자의 개수")

#[]안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위(From - To)를 의미
upper_case = re.compile('[A-Z]')
lower_case = re.compile('[a-z]')
num_case = re.compile('[0-9]')
etc_case = re.compile('[^0-9a-zA-Z]')   #^는 제외한다는 의미

#findall()메소드는 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다.
upper = upper_case.findall(f"{str}")
lower = lower_case.findall(f"{str}")
num = num_case.findall(f"{str}")
etc = etc_case.findall(f"{str}")

print(f"대문자 = {len(upper)}\n소문자 = {len(lower)}\n숫자 = {len(num)}\n특수문자 = {len(etc)}")    #\n은 이스케이프, len()함수는 리스트길이