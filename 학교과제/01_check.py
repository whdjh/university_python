def check(words):
    count = 0							   #문자열의 개수를 저장하는 변수
    word = []							   #동일한 문자열을 저장할 리스트
    for i in range(len(words)):  	   	   #0부터 문자열 길이만큼 range(n)이면 n - 1까지 보니까 n개 배교하기 위해 리스트 길이만큼 비교한다
        #여기서 이중 for문을 사용해서 풀 수 있지만 우리가 원하는것은 리스트내 문자열 중 0번째 인덱스와 마지막 인덱스의 비교만 원하므로 비교횟수 낭비없이 인덱스로 접근하여 비교횟수를 최대한 적게 사용한다.
        if words[i][0] != words[i][-1]:    #가장 왼쪽 문자와 가장 오른쪽 문자를 비교하여 문자가 다르면
            continue        		 	   #지금의 if문을 넘어가고 for문을 다음 순서로 돌린다. break과의 차이는 종료시키는 여부로 볼 수 있다 
        if words[i][0] == words[i][-1]:	   #가장 왼쪽 문자와 가장 오른쪽 문자를 비교하여 문자가 같으면
            count += 1					   #문자열의 개수를 하나씩 늘려간다.
            word.append(words[i])		   #리스트 내 동일한 문자열을 새로운 리스트에 넣어준다.
    
    return f"문자열의 개수 = {count}\n동일한 문자열 = {word}"	#f문자열 포맷 활용해서 return 해준다. \n은 개행하는 이스케이프.

words = ['aba', 'xyz', 'abcA', '20211020', 'python_p', 'ABCBA', '11'] 

print(check(words))                 #결과값 출력