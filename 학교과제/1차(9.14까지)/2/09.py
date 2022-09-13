#어느 평가위원회는 평가 점수 중 최고점과 최저점을 제외한 점수들의 평균을 최종 평가 점수로 부여하려고 한다.
A = [85, 96, 78, 88, 81, 92, 73]

A.sort()

print(A)

del A[0]

A.pop()

result = sum(A)

average_A = result / len(A)

print(average_A)