#버블정렬 알고리즘을 패스별로 최댓값을 오른편으로 보내는 것과 
#최솟값을 왼편으로 보내는 과정을 번갈아 실행하도록 수정하라.

def bubble_sort_short(a_list):
    for i in range(len(a_list) - 1, 0, -1):
        exchanges = False    # 패스 기간 내 자리교환 발생 여부 저장
        flag = 1
        if flag == 1:
            for j in range(i):
                if a_list[j] > a_list[j + 1]:
                    exchanges = True
                    a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
            flag = 0
            print(f"최대 : {a_list}")
            
        if flag == 0:
            for j in range(i, 0, -1):
                if a_list[j] < a_list[j - 1]:
                    exchanges = True
                    a_list[j], a_list[j - 1] = a_list[j - 1], a_list[j]
            print(f"최소 : {a_list}")
                    
            

        if not exchanges:   # 패스 기간 동안 자리교환이 발생하지 않은 경우 조기종료
            print("조기종료!")
            break

                   
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort_short(a_list)
print(a_list)