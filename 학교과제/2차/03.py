#무한 원숭이 정리에서 작성한 infinite_monkey() 함수가 아래 기능을 만족하도록 수정하라
#생성된 문자열 중에서 정확한 위치에서 사용된 문자는 그대로 두고 그렇지 않은 문자만 업데이트한다.
import random

def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
        
    return res

def score(goal, teststring):
    numScore = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numScore = numScore + 1
    
    return numScore / len(goal)

def infinite_monkey():
    goalstring = "methinks it is like a weasel"
    newstring = generateOne(28)
    best = 0
    newscore = score(goalstring, newstring)
    while newscore < 1:
        if newscore >= best:
            print(newscore, newstring)
            best = newscore
        newstring = [newstring[i] if newstring[i] == goalstring[i] else generateOne(1) for i in range(28)]
        # newstring = generateOne(28)
        newscore = score(goalstring, newstring)
        
infinite_monkey()