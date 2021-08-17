from collections import defaultdict

def read_keylog():
    f=open("./p079_keylog.txt",'r')
    data=[]
    for l in f.readlines():
        data+=[int(l)]
    return data    

def get_keycode_numbers(data):
    ordering={}
    for n in data:
        nums=str(n)
        for i,d in enumerate(nums):
            if d not in ordering:
                ordering[d]=[]
            for l in nums[:i]:
                if l not in ordering[d]:
                    ordering[d].append(l)
    
    return ordering

def sort_keycode_numbers(ordering):
    keycode=[]
    for i in range(0,len(ordering)):
        for n,v in ordering.items():
            if v==[] and len(keycode)==0:
                keycode.append(n)
            else:
                if sorted(keycode)==sorted(v):
                    keycode.append(n)
    return keycode                
        

def main():
    data=read_keylog()
    ordering=get_keycode_numbers(data)
    keycode=sort_keycode_numbers(ordering)
    return keycode


print(main())
