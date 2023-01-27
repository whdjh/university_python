import random

a = random.randint(0, 100)

print(f"뽑힌점수 : {a}")

if(a >= 90):
    print("장학생입니다.")
    
elif(a >= 60):
    print("합격생입니다.")
    
else:
    print("불합격입니다.")