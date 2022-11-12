a = int(input("첫번째 숫자를 입력하시오 "))
b = int(input("두번째 숫자를 입력하시오 "))

while(True):
    choice = input("1. 덧셈, 2. 뺄셈, 3. 곱셈, 4. 나눗셈, 5. 종료")
    if choice == '1':
        print(f"덧셈: ({a} + {b}) = {a + b}")
        
    elif choice == '2':
        print(f"덧셈: ({a} - {b}) = {a - b}")
        
    elif choice == '3':
        print(f"덧셈: ({a} * {b}) = {a * b}")
        
    elif choice == '4':
        print(f"덧셈: ({a} / {b}) = {a / b}")
        
    else:
        print("계산기가 종료되었습니다.")
        break