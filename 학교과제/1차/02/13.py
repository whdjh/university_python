#주어진 정수를 오름차순으로 정렬하여, 리스트 형태로 반환하는 int2sorted_list() 함수를 작성하라. 
#단, 양의 정수만 입력값으로 사용한다.
def int2sorted_list(an_int):
    assert an_int > 0
    str_list = str(an_int)
    n_list = list(str_list)
    result = sorted(n_list)
    return result

print(int2sorted_list(32145))

