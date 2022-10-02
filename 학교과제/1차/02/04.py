s = '산토끼 토끼야 어디로 가느냐'
rev_s = '끼토산 야끼토 로디어 냐느가'

def reverse_words(s):
    for i in s:
        result = ' '.join(i[::-1] for i in s.split())
    return result

print(reverse_words(s))
 
assert reverse_words(s) == rev_s 