student_tup = (('211101', '최정인', "010-1234-4567", 4.0), ('211102', '김하나', "010-2222-3333", 4.5))

student_dic = {}

print("학생의 정보 목록")
for i in range(len(student_tup)):
    for j in range(len(student_tup[i])):
            student_dic[student_tup[i][0]] = [student_tup[i][1:j + 1]] 

print(student_dic)
    
n = 0

for i in range(len(student_tup)):
    n += student_tup[i][-1]
    
print(f"전체 학생의 학점 평균 : {n // len(student_tup)}")