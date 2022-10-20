#아래 함수는 두 문자열의 어구전철 여부를 확인하기 위해 각 문자의 사용 빈도수를 활용한다.
#그런데 위 함수는 두 문자열에 각각 하나씩 빈도수 저장 어레이를 사용한다. 
#하나의 빈도수 저장 어레이만 사용하도록 위 알고리즘을 수정하라. 수정된 알고리즘의 시간복잡도를 계산하라.
def anagram_solution_4(s1, s2):
    
    # 빈도수 저장 용도 리스트
    c1 = [0] * 26

    # s1에 포함된 문자들의 빈도수
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1          # 기본 계산단위: 카운트        
        
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c1[pos] = c1[pos] - 1
        
    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == 0:             # 기본 계산단위: 항목 비교
            j = j + 1
        else:
            still_ok = False
    return still_ok
        
s1 = 'python'
s2 = 'ythonp'
print(anagram_solution_4(s1, s2))