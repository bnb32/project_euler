coins=[1,2,5,10,20,50,100]

def combos(N):
    count=1
    rem0=N
    for n0 in range(0,rem0//coins[0]+1):
      rem1=rem0-n0*coins[0]
      for n1 in range(0,rem1//coins[1]+1):
        rem2=rem1-n1*coins[1]
        if rem2 % 5 == 0:
          for n2 in range(0,rem2//coins[2]+1):
            rem3=rem2-n2*coins[2]
            for n3 in range(0,rem3//coins[3]+1):
              rem4=rem3-n3*coins[3]
              for n4 in range(0,rem4//coins[4]+1):
                rem5=rem4-n4*coins[4]
                for n5 in range(0,rem5//coins[5]+1):
                  rem6=rem5-n5*coins[5]
                  for n6 in range(0,rem6//coins[6]+1):
                    rem=rem6-n6*coins[6]
                    if rem==0:
                      count+=1
    return count

if __name__=="__main__":
    print(combos(200))
