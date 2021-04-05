# 3 sayıdan en büyük olanı bulma

s1 = int(input("1.Sayıyı giriniz :"))
s2 = int(input("2.Sayıyı giriniz :"))
s3 = int(input("3.Sayıyı giriniz :"))

if (s1>s2) and (s1>s3):
    print("En büyük sayı :",s1) 
elif (s2>s1) and (s2>s3):
    print("En büyük sayı :",s2) 
else:
    print("En büyük sayı :",s3) 
