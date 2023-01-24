s = input()
s_list = []

for i in s:
    s_list.append(s)
    s = s[1:]
    
for i in sorted(s_list):
    print(i)