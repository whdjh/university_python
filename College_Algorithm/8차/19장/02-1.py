def edit_distance(str1,str2):
  P = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
  # 첫째 문자열의 길이가 i, 둘째 문자열의 길이가 j일 때, 두 문자열의 편집 거리

  for i in range(len(str1)+1):
    P[0][i] = i * 20
  for j in range(len(str2)+1):
    P[j][0] = j * 20
  # 기존 편집 거리 코드와 다른점 : 기존 편집거리 문제는 치환의 거리를 1로 잡았다.
  # 따라서 양쪽 모두 문자가 추가되었을 때 거리가 1만 증가했다.
  # 위 문제는 치환이 삭제 + 추가로 거리가 2인 부분이 다르다.
  for j in range(1,len(str1)+1):
    for i in range(1,len(str2)+1):
      if str1[i-1] == str2[j-1]:
        P[j][i] = P[j-1][i-1] + 5
      else:
        P[j][i] = min(P[j-1][i], P[j][i-1]) + 20
  return P[-1][-1]

print(edit_distance("algorithm", "alligator"))