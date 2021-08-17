import string

scores={l: i+1 for i,l in enumerate(string.ascii_lowercase)}

def wordVal(s):
    score=0
    for d in s.lower():
        score+=scores[d]
    return score    

def triNum(n):
    return n*(n+1)//2

def isTriWord(s):
    score=wordVal(s)
    minN=int((2*score)**0.5)
    maxN=minN+1
    for i in range(minN,maxN+1):
        if triNum(i)==score:
            return True
    return False        

def main():
    f=open('./p042_words.txt','r')
    words=f.readline().split(',')
    count=0
    for w in words:
        if isTriWord(w.strip('"')): 
            count+=1
    return count    

if __name__=="__main__":
    print(main())
