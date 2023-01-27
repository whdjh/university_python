#기존 튜플 자료형생성
student_tup = (('211101', '최정인', "010-1234-4567", 4.0), ('211102', '김하나', "010-2222-3333", 4.5))

student_dic = {}    #딕셔너리로 바꿔서 출력하기위해 딕셔너리 자료형 생성

print("학생의 정보 목록")   #출력메세지

#이중for문을 이용해서 키와 키값을 딕셔너리에 넣음
for i in range(len(student_tup)):   #튜플의 길이만큼돈다.
    for j in range(len(student_tup[i])):    #튜플안의 튜플의 길이만큼돈다.
            student_dic[student_tup[i][0]] = [student_tup[i][1:j + 1]]  #키와 키값을 딕셔너리에 넣는다.

print(student_dic)  #딕셔너리 출력
    
n = 0   #평균을 구하기위해 모든 학점을 더해줄것이므로 선언후 0으로 초기화한다.

#튜플의 길이만큼 돌것임.
for i in range(len(student_tup)):
    n += student_tup[i][-1] #튜플안의 튜플에서 마지막 요소가 학점에 해당하므로 n변수에 계속 넣어준다
    
print(f"전체 학생의 학점 평균 : {n // len(student_tup)}")   #튜플의 길이는 학생수가 되므로 길이를 나눠주면 평균이 나오게 된다.