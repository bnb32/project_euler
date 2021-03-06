words={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

def num_letters(N):
    if 1<=N<=20:
        return len(words[N])
    
    elif 20<N<100:
        tmp=str(N)
        ones=int(tmp[-1])
        tens=int(tmp)-int(ones)
        return len(words[tens])+num_letters(ones)
    
    elif 100<=N<1000:
        tmp=str(N)
        hundreds=int(tmp[0])
        tens=int(tmp[1:])
        if tens!=0:
            return len(words[hundreds]+'hundred')+len('and')+num_letters(tens)
        else:
            return len(words[hundreds]+'hundred')
    
    elif N==1000:
        return len('one')+len('thousand')
    
    else:
        return 0


def sum_letters():
    letters=0
    for i in range(1,1001):
        letters+=num_letters(i)
    return letters    

if __name__=="__main__":
    print(sum_letters())
