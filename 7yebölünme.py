# n den m e kadar sayıların 7ye tam bölünenelerin toplamı (n ve m karşıdan alınacaktır)
while True: 
    n = int(input("Başlangıç sayısı :"))
    m = int(input("Bitiş sayısı :"))
    if n>m :
        print("n mden küçük olmalı")
    else :
        break

toplam = 0
i = 0
for i in range(n,m):
    if i%7==0 :
        toplam += i
print("7ye tam bölünen sayıların toplamı :", toplam)
