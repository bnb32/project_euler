from itertools import permutations
import string

alphabet=[l for l in string.ascii_lowercase]

def decode(nums,code):
    words=[]
    new_nums=[]
    w=''
    for i,n in enumerate(nums): 
        num=int(n)^ord(code[i%len(code)])
        tmp=chr(num)
        new_nums.append(num)
        if tmp==' ': 
            words.append(w)
            w=''
        else: w+=tmp
    words.append(w)    
    return words,sum(new_nums)

def passwords():
    perms=permutations(alphabet,3)
    pwds=[p for p in perms]
    return pwds

def main():
    pwds=passwords()
    nums=open('./p059_cipher.txt','r').readline().split(',')
    for i in range(0,len(pwds)):
        words,val=decode(nums,pwds[i])
        if 'the' in words: return (words,val,pwds[i])
    
if __name__=="__main__": print(main())    
