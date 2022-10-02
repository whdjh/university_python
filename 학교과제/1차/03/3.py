participants = {'1월3일' : ['현성', '문정', '현무', '강현'], 
                '2월10일' : ['문정', '강현', '정훈'], 
                '3월7일' : ['현성', '연아', '현무', '지아']}
participants['3월7일'] = ['현성', '연아', '현무', '지아', '강현']
result = participants.get('3월7일')
print(f'3월7일 모임에는 {result}, 총 5명이 참석했습니다.')

participants = {'1월3일' : ['현성', '문정', '현무', '강현'], 
                '2월10일' : ['문정', '강현', '정훈'], 
                '3월7일' : ['현성', '연아', '현무', '지아']}

def attended(name):
    result = participants.get('1월3일')
    print(result)
    if name in result:
      fin = True
    else:
      fin = False

    return fin

print(attended('현성'))