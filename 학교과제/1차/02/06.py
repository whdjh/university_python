s = 'printMessage'
tmp1 = ''
tmp2 = ''

def camel2pothole(s):
    cnt = 0
    for i in s:
        cnt = cnt + 1
        if 'A' <= i <= 'Z' :
            break
    tmp1 = s[cnt - 1:]
    tmp2 = s[0:cnt - 1]
    str = tmp2 + '_' + tmp1
    result = str.lower()
    return result

print(camel2pothole(s))