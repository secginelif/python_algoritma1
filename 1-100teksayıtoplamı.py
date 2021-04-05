#1.yol mod alarak
n =int(input("1 ile kaça kadar olsun :"))
toplam = 0

for i in range(n):
    if i%2==1 :
        toplam += i
print(toplam)

#2.yol döngü ile
toplam = 0
i  = 0

for i in range(1,n,2):
    toplam += i
print("Toplam :",toplam)