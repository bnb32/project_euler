def isLychrel(N):
    i=0
    s=str(N)
    while s!=s[::-1] and i<=50 or s==s[::-1] and i==0:
        s=str(int(s)+int(s[::-1]))
        i+=1
    if s!=s[::-1]: 
        return True
    else:
        return False

def main():
    count=0
    for n in range(1,10**4):
        if isLychrel(n): count+=1
    return count

if __name__=="__main__": print(main())    
