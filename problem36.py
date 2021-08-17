def decToBin(N):
    s=''
    while N>1:
        s=str(N%2)+s
        N//=2
        
    s=str(N%2)+s
    return int(s)

def isPalindrome(N):
    if str(N)==str(N)[::-1]:
        return True
    return False    

def palindromes():
    pals=[]
    for i in range(1,10**3):
        pals.append(int(str(i)+str(i)[::-1]))
        pals.append(int(str(i)+str(i)[:-1][::-1]))
        
    return pals        

def main():
    return sum(n for n in palindromes() if isPalindrome(decToBin(n)))

if __name__=="__main__":
    print(main()) 
