#str1과 str2 두 개의 문자열이 주어졌을 때 str1를 이용해서 str2로 변환하는 데 필요한 최소 비용,
#즉 편집 거리(edit distance)을 계산한다.
#단, 변환은 다음 세 가지 방식 중에 하나를 연속적으로 선택해서 진행한다.

#하나의 문자를 그대로 사용. 비용은 5.
#하나의 문자를 삭제. 비용은 20.
#하나의 문자를 추가. 비용은 20
#예를 들어, "algorithm"에서 "alligator"로의 변환에 필요한 최소 비용은 다음과 같이 구할 수 있다.

#처음 두 개의 문자 "al"은 동일하기 때문에 그대로 사용. 비용 10.
#"gorithm"에서 "ligator"로의 변환에 필요한 최소 비용 계산.
#따라서 두 개의 문자열의 길이의 합이 적은 경우의 편집 거리를 이용하여 보다 긴
#두 문자열의 편집 거리를 동적계획법으로 계산할 수 있다.
#1. 앞서 설명한 동적계획법을 적용했을 때 최소 비용이 계산되는 것을 보장하기 위해 먼저 최적의 원칙이 보장됨을 설명

#2. 두 개의 문자열이 주어졌을 때 두 문자열의 편집 거리를 계산하는 함수 edit_distance()를 동적계획법으로 구현
#힌트: len(str1) = m, len(str2) = n 일 때,
#(m+1) x (n+1) 모양의 2차원 행렬을 P라 할 때 P[i][j]가 다음 성질을 만족해야 한다.

#첫째 문자열의 길이가 i, 둘째 문자열의 길이가 j일 때, 두 문자열의 편집 거리