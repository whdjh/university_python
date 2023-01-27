def	Changes(goods, amount):                 #goods와 amount 리스트를 매개변수로 받는 함수생성
    musinsa = {}							#딕셔너리로 접근하기위해 빈 딕셔너리생성
    if len(goods) != len(amount):           #길이가 다르면 오류!
        return                              #아무것도 출력해주지않음!
    for i in range(len(goods)):				#상품들을 넣어주자. 여기서 이중포문이 필요없는 이유는 상품의 갯수와 가격의 갯수가 같기 때문이다.
        musinsa[goods[i]] = amount[i]	    #딕셔너리[키] = 값 하면 딕셔너리가 추가된다.

    x = input("구매 상품을 입력세요.")			 #입력을 받는다
    y = int(input("지불 금액을 입력하세요."))	 #가격은 int형이니까 input의 기본은 문자열이여서 강제 형변환을 시켜준다.
    if x == "티셔츠":						 #만약 x가 티셔츠라면
        count = y - musinsa["티셔츠"]		 #딕셔너리[키]하면 값에 대해 접근가능하다
    elif x == "바지":						#만약 x가 바지라면
        count = y - musinsa["바지"]			 #딕셔너리[키]하면 값에 대해 접근가능하다
    elif x == "반바지":						 #만약 x가 반바지라면	
        count = y - musinsa["반바지"]		 #딕셔너리[키]하면 값에 대해 접근가능하다
    elif x == "스커트":						 #만약 x가 스커트라면
        count = y - musinsa["스커트"]		 #딕셔너리[키]하면 값에 대해 접근가능하다
    else:								   #그것도 아니라면 = 만약 x가 모자라면
        count = y - musinsa["모자"]			#딕셔너리[키]하면 값에 대해 접근가능하다
    return count						   # 거스름돈 출력
    
goods = ["티셔츠", "바지", "반바지", "스커트", "모자"]  #goods 즉, 상품에 해당하는 리스트 생성
amount = [20000, 25000, 15000, 18000, 10000]     #amount 즉, 상품의 가격에 해당하는 리스트 생성
print(Changes(goods, amount))                    #출력