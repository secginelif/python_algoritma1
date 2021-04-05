bolen_sayac =0
for i in range(3,100):
    bolen_sayac = 0 
    for a in range(2,i):
        if (i%a==0):
            bolen_sayac +=1
    if bolen_sayac==0:
        print("{} asaldır ".format(i))