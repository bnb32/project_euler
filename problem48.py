def main():
    summa=0
    for i in range(1,1001):
        summa+=i**i
    return str(summa)[-10:]

if __name__=="__main__": print(main())    
