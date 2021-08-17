card_vals={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
hand_vals={'HC':0,'2K':1,'2P':2,'3K':3,'S':4,'F':5,'FH':6,'4K':7,'SF':8,'RF':9}

def is_straight(sorts):
    tmp=[sorts[i]['value'] for i in sorts]
    if tmp[1]==tmp[0]+1 and tmp[2]==tmp[1]+1 and tmp[3]==tmp[2]+1 and tmp[4]==tmp[3]+1: 
        HC=sorts[4]['value']
        return True,HC
    elif tmp==[2,3,4,5,14]: 
        HC=5
        return True,HC
    return False,0

def is_flush(sorts):
    suits=[sorts[i]['suit'] for i in sorts]
    if suits.count(suits[0])==5: 
        HC=sorts[4]['value']
        return True,HC
    return False,0

def is_Nkind(sorts,N):
    for i in sorts:
        if sorts[i]['count']==N: 
            HC=sorts[i]['value']
            return True,HC
    return False,0

def is_fullhouse(sorts):
    HC=0
    for i in sorts:
        if sorts[i]['count']==3:
            val=sorts[i]['value']
            if val>HC: HC=val
            for j in sorts:
                if sorts[j]['count']==2:
                    return True,HC
    return False,0

def is_twopair(sorts):
    HC=0
    for i in sorts:
        if sorts[i]['count']==2:
            val=sorts[i]['value']
            if val>HC: HC=val
            for j in sorts:
                if sorts[j]['value']!=sorts[i]['value'] and sorts[j]['count']==2:
                    tmp=sorts[j]['value']
                    if tmp>HC: HC=tmp
                    return True,HC
    return False,0

def sortedCards(cards):
    vals=[c[0] for c in cards]
    suits=[c[1] for c in cards]
    idx=sorted(range(len(vals)),key=lambda k: card_vals[vals[k]])
    return {k: {'value':card_vals[vals[idx[k]]],'suit':suits[idx[k]],'count':vals.count(vals[idx[k]])} for k in range(0,5)}

def poker_hand(cards):
    
    sorts=sortedCards(cards)

    tmp=is_straight(sorts)
    if tmp[0] and is_flush(sorts)[0]: 
        if sorts[4]['value']==14:
            return 'RF',14
        else:
            return 'SF',tmp[1]

    tmp=is_Nkind(sorts,4)
    if tmp[0]: return '4K',tmp[1]

    tmp=is_fullhouse(sorts)
    if tmp[0]: return 'FH',tmp[1]

    tmp=is_flush(sorts)
    if tmp[0]: return 'F',tmp[1]

    tmp=is_straight(sorts)
    if tmp[0]: return 'S',tmp[1]

    tmp=is_Nkind(sorts,3)
    if tmp[0]: return '3K',tmp[1]

    tmp=is_twopair(sorts)
    if tmp[0]: return '2P',tmp[1]

    tmp=is_Nkind(sorts,2)
    if tmp[0]: return '2K',tmp[1]

    return 'HC',sorts[4]['value']

def next_highest(sorts,HC):
    for i in range(4,0,-1):
        if sorts[i]['value']!=HC:
            return sorts[i]['value']

def main():
    cards=[]
    count=0
    f=open('./p054_poker.txt','r')
    for l in f.readlines():
        cards.append(l.split())
    for i in range(0,len(cards)):    
        cards1=cards[i][0:5]
        cards2=cards[i][5:10]
        hand1=poker_hand(cards1)
        rank1=hand1[0]
        HC1=hand1[1]
        hand2=poker_hand(cards2)
        rank2=hand2[0]
        HC2=hand2[1]
        
        if hand_vals[rank1]>hand_vals[rank2]: 
            count+=1
        elif hand_vals[rank1]==hand_vals[rank2]:
            if HC1>HC2: 
                count+=1
            elif HC1==HC2:
                HC1=next_highest(sortedCards(cards1),HC1)
                HC2=next_highest(sortedCards(cards2),HC2)
                if HC1>HC2: 
                    count+=1
                elif HC1==HC2:
                    print('TIE')
    return count            

if __name__=="__main__": print(main())    
