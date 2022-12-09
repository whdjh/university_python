def	Changes(goods, amount):
    musinsa = {}							#딕셔너리로 접근하기위해 빈 딕셔너리생성
    for i in range(len(goods)):				#상품들을 넣어주자
        for j in range(len(amount)):		#그 상품에 해당하는 값을 넣어주자
            musinsa[goods[i]] = amount[i]	#딕셔너리[키] = 값 하면 딕셔너리가 추가된다.
    
    x = input("구매 상품을 입력세요.")			 #입력을 받는다
    y = int(input("지불 금액을 입력하세요."))	 #가격은 int형이니까 input의 기본은 문자열이여서 강제 형변환을 시켜준다.
    if x == "티셔츠":						 # 이건 너가해라 수정아
        count = y - musinsa["티셔츠"]		 #딕셔너리[키]하면 값에 대해 접근가능하다
    elif x == "바지":						# 이건 너가해라 수정아
        count = y - musinsa["바지"]			#딕셔너리[키]하면 값에 대해 접근가능하다
    elif x == "반바지":						 # 이건 너가해라 수정아	
        count = y - musinsa["반바지"]		#딕셔너리[키]하면 값에 대해 접근가능하다
    elif x == "스커트":						 # 이건 너가해라 수정아
        count = y - musinsa["스커트"]		#딕셔너리[키]하면 값에 대해 접근가능하다
    else:								   # 이건 너가해라 수정아
        count = y - musinsa["모자"]			#딕셔너리[키]하면 값에 대해 접근가능하다
    return count						   # 거스름돈 출력
    
goods = ["티셔츠", "바지", "반바지", "스커트", "모자"]
amount = [20000, 25000, 15000, 18000, 10000]

print(Changes(goods, amount))