import random
from operator import *

shapes = ['♠', '♥', '◆', '♣']
nums = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Card:
    def __init__(self, shape, num):
        self.shape = shape
        self.num = num
    #[] 오퍼레이터 오버라이딩
    def __getitem__(self, key):
        if key == 0:
            return self.shape
        elif key == 1:
            return self.num
        
    def __str__(self):
        return f"({self.num}, {self.shape})"
    
    def __repr__(self):
        return self.__str__()
        
class Deck:
    def __init__(self):
        self.cards = []
        for shape in shapes:
            for num in nums:
                self.cards.append(Card(shape, num))
        self.cards.append(Card('Joker', 'colored'))
        self.cards.append(Card('Joker', 'black'))

    def draw(self):
        return self.cards.pop()
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
deck = Deck()
random.shuffle(deck.cards)

# 플레이어에게 카드 나누기

player1 = []
player2 = []

for i in range(7):
    player1.append(deck.draw())
    player2.append(deck.draw())

# 낸 카드에 하나 올려놓기
put = []
put.append(deck.draw())
        
global count

# 특수상황
def special(selected, isplayer2):
    global count  

    #한 번 더: K를 내면 카드를 한 장 더 낼 수 있고, J를 내면 한 턴을 건너뜀
    if(eq(selected[1],'K') or eq(selected[1],'J')):
        if isplayer2:
            turn(players[1],isplayer2)
        else:
            turn(players[0],isplayer2)

def turn(hand, isplayer2):
    # 전역 변수 접근
    global put, deck, count 
    # 이름 정하기
    if isplayer2:
        name = "플레이어2"
    else:
        name = "플레이어1"
    # 차례
    print('\n')
    print(name, "의 차례입니다.")
    print("현재 패 >>", hand)
    print("놓여진 카드 >>", put[-1])
    # 공격일 때, 가능한 카드 리스트 반환
    if isplayer2:
        def getAvailable2(hand, last_card):
            global count    
            available = []
            if(last_card[1]=='2'):
                for card in hand:
                    if (card[1] == last_card[1] or card[0] == 'Joker'
                        or (card[0]==last_card[0] and card[1] == 'A')):
                        available.append(card)
            elif(last_card[1]=='A'):
                for card in hand:
                    if (card[1] == last_card[1] or card[0] == 'Joker'):
                        available.append(card)
            elif(last_card[0]=='Joker'):
                for card in hand:
                    if (card[0] == 'Joker'):
                        available.append(card)          
            #다음 턴을 위해 non_attack 상태로 세팅         
            count = 'non_attack'
            return available    

        # 가능한 카드 리스트를 반환
        def getAvailable(hand, last_card):
            global count
            available = []    
            for card in hand:
                if (card[0] == last_card[0]
                    or card[1] == last_card[1]
                    or card[0] == 'Joker'
                    or put[-1][0] == 'Joker'):
                    available.append(card)           
            #공격상황을 대비해 attack으로 세팅        
            count = 'attack'
            return available
        # 가능한 카드
        # 공격 상황(2,A,Joker)
    
        if(put[-1][1] in ['2','A','colored','black'] and eq(count,"non_attack")):
            available = getAvailable(hand, put[-1])
        elif(put[-1][1]in ['2','A','colored','black']):
            available = getAvailable2(hand, put[-1])
        # 일반상황        
        else:
            available = getAvailable(hand, put[-1])          
        print("낼 수 있는 카드:", available)
        # 낼 수 있는 카드가 있는 경우
        if len(available) > 0:
            if isplayer2:
                i= int(input("몇 번째 카드를 내시겠습니까?"))
                i -= 1
                selected = available[i]  
                print("플레이어2가", selected, "를 냈습니다.")
            else:
                i= int(input("몇 번째 카드를 내시겠습니까?"))
                i -= 1
                selected = available[i]         
            hand.remove(selected)
            put.append(selected)
            #특수상황인지 판단
            special(selected,isplayer2)
        # 낼 수 있는 카드가 없는 경우
        else:
            #뽑을 수 있는 카드가 없으면 무승부
            if(len(deck.cards) == 0):            
                print("무승부")
                return True
            #공격 상황에 따라 먹는 경우
            if(count == 'non_attack' and put[-1][1]== '2'):
                print(name,"가 방어할 카드가 없어 2장 먹습니다.")
                for i in range(1,3):
                    hand.append(deck.draw())
            elif(count == 'non_attack' and put[-1][1]== 'A'):
                print(name,"가 방어할 카드가 없어 3장 먹습니다.")
                for i in range(1,4):
                    hand.append(deck.draw())
            elif(count == 'non_attack' and put[-1][1]== 'colored'):
                print(name,"가 방어할 카드가 없어 8장 먹습니다.")
                for i in range(1,9):
                    hand.append(deck.draw())            
            elif(count == 'non_attack' and put[-1][1]== 'black'):
                print(name,"가 방어할 카드가 없어 5장 먹습니다.")
                for i in range(1,6):
                    hand.append(deck.draw())
            else:
                print(name, "가 낼 수 있는 카드가 없어 먹습니다.")
                hand.append(deck.draw())
        #수중에 카드가 없으면 승리
        if len(hand) == 0:
            print(name, "가 이겼습니다!")
            return True
        else:
            return False
    else:
        def getAvailable2(hand, last_card):
            global count    
            available = []
            if(last_card[1]=='2'):
                for card in hand:
                    if (card[1] == last_card[1] or card[0] == 'Joker'
                        or (card[0]==last_card[0] and card[1] == 'A')):
                        available.append(card)
            elif(last_card[1]=='A'):
                for card in hand:
                    if (card[1] == last_card[1] or card[0] == 'Joker'):
                        available.append(card)
            elif(last_card[0]=='Joker'):
                for card in hand:
                    if (card[0] == 'Joker'):
                        available.append(card)          
            #다음 턴을 위해 non_attack 상태로 세팅         
            count = 'non_attack'
            return available    

        # 가능한 카드 리스트를 반환
        def getAvailable(hand, last_card):
            global count
            available = []    
            for card in hand:
                if (card[0] == last_card[0]
                    or card[1] == last_card[1]
                    or card[0] == 'Joker'
                    or put[-1][0] == 'Joker'):
                    available.append(card)           
            #공격상황을 대비해 attack으로 세팅        
            count = 'attack'
            return available
        # 가능한 카드
        # 공격 상황(2,A,Joker)
    
        if(put[-1][1] in ['2','A','colored','black'] and eq(count,"non_attack")):
            available = getAvailable(hand, put[-1])
        elif(put[-1][1]in ['2','A','colored','black']):
            available = getAvailable2(hand, put[-1])
        # 일반상황        
        else:
            available = getAvailable(hand, put[-1])          
        print("낼 수 있는 카드:", available)
        # 낼 수 있는 카드가 있는 경우
        if len(available) > 0:
            if isplayer2:
                i= int(input("몇 번째 카드를 내시겠습니까?"))
                i -= 1
                selected = available[i]  
                print("플레이어2가", selected, "를 냈습니다.")
            else:
                i= int(input("몇 번째 카드를 내시겠습니까?"))
                i -= 1
                selected = available[i]         
            hand.remove(selected)
            put.append(selected)
            #특수상황인지 판단
            special(selected,isplayer2)
        # 낼 수 있는 카드가 없는 경우
        else:
            #뽑을 수 있는 카드가 없으면 무승부
            if(len(deck.cards) == 0):            
                print("무승부")
                return True
            #공격 상황에 따라 먹는 경우
            if(count == 'non_attack' and put[-1][1]== '2'):
                print(name,"가 방어할 카드가 없어 2장 먹습니다.")
                for i in range(1,3):
                    hand.append(deck.draw())
            elif(count == 'non_attack' and put[-1][1]== 'A'):
                print(name,"가 방어할 카드가 없어 3장 먹습니다.")
                for i in range(1,4):
                    hand.append(deck.draw())
            elif(count == 'non_attack' and put[-1][1]== 'colored'):
                print(name,"가 방어할 카드가 없어 8장 먹습니다.")
                for i in range(1,9):
                    hand.append(deck.draw())            
            elif(count == 'non_attack' and put[-1][1]== 'black'):
                print(name,"가 방어할 카드가 없어 5장 먹습니다.")
                for i in range(1,6):
                    hand.append(deck.draw())
            else:
                print(name, "가 낼 수 있는 카드가 없어 먹습니다.")
                hand.append(deck.draw())
        #수중에 카드가 없으면 승리
        if len(hand) == 0:
            print(name, "가 이겼습니다!")
            return True
        else:
            return False
    
# 게임 시작
players = [player1, player2]
i = 0
while True:
    # i가 0이 아니면 컴퓨터라고 간주
    if i != 0:
        isplayer2 = True
    else:
        isplayer2 = False

    if turn(players[i], isplayer2):
        break

    # 차례 조정
    i += 1
    if i >= len(players):
        i -= len(players)