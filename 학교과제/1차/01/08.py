song = "When you are smiling, the whole world smiles with you"

count = 0
for i in song:
	if i == "a":
		count += 1
print(count)

count = 0
for i in song:
    if i == "w" or i == "W":
        count += 1
print(count)