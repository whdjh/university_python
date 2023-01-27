#mergesort() 함수에 사용된 알고리즘을 수정하여 재귀에 사용된 슬라이싱 
#대신 구간 지정방식을 사용하는 재귀 합병 알고리즘을 구현하라.
#힌트: 합병을 담당하는 함수를 따로 정의해서 분할 재귀함수에 활용한다.

def mergesort(a_list, left, right):
  #left는 첫번째 인덱스, right는 마지막 인덱스를 뜯한다. 따라서 초기 입력시 left = 0, right = len(a_list) - 1이 되어야 한다.
	if left >= right:   #예외처리 left가 right보다 크다면 return시킴, 정렬할 필요가 없음
		return
	mergesort(a_list, left, (left + right) // 2)    #슬라이싱으로 처리한 부분을 재귀로 처리
	mergesort(a_list, (left + right) // 2 + 1, right)   #슬라이싱으로 처리한 부분을 재귀로 처리
	return sorting(a_list, left, right)   #합병시키러 간다.

#합병을 담당하는 함수. 합병정렬 알고리즘 생각하면서 풀어 나가면된다.
def sorting(a_list, left, right):
	mid = (left + right) // 2
	i = left
	j = mid + 1
	tmp = []

	while i <= mid and j <= right:
		if a_list[i] <= a_list[j]:
			tmp.append(a_list[i])
			i += 1
		else:
			tmp.append(a_list[j])
			j += 1

	while i <= mid:
		tmp.append(a_list[i])
		i += 1

	while j <= right:
		tmp.append(a_list[j])
		j += 1

	for k in range(left, right + 1):
		a_list[k] = tmp[k - left]
  
	return a_list