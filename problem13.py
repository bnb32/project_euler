f=open("./problem13.txt",'r')
nums=f.readlines()

def sum_nums():
    tmp=0
    for n in nums:
        tmp+=int(n)
    return str(tmp)[0:10]

if __name__=="__main__":  
    print(sum_nums())
