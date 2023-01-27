word_list = ["cat", "dog", "rabbit"]
new_list = []

for x in word_list:
    for y in x: 
    	if y:
        	new_list.append(y)
print(f'중복 허용 출력값 1: {new_list}')

result = []
for value in new_list:
    if value not in result:
        result.append(value)
        
print(f'중복 없는 출력값 2: {result}')