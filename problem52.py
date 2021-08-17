def check_digits(N):
    for i in range(2,7):
        tmp=i*N
        for d in str(tmp):
            if str(tmp).count(d)!=str(N).count(d):
                return False
    return True

def main():
    n=1
    while True:
        if check_digits(n): return n
        n+=1
    
if __name__=="__main__": print(main())
