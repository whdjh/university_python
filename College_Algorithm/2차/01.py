word_list = ["cat", "dog", "rabbit"]
new_list = []

for x in word_list:
    for y in x: 
    	if y:
        	new_list.append(y)

result = []
for value in new_list:
    if value not in result:
        result.append(value)

print(result)