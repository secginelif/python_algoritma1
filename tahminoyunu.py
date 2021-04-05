import random as r

sayi = int(input ("0 ile kaç arasında olsun? "))
rastgele_sayi = r.randint(1,sayi)


while True:
    tahmin = int(input("0 ile {} arasında tahminizi Girin: ".format(sayi)))

    if tahmin == rastgele_sayi:
        for i in range(5):
            print("Tahmininiz Doğru") 
        break
    elif tahmin != rastgele_sayi:
        print("Tahmininiz Doğru Değil")
        print("Tutulan Sayı {} ".format(rastgele_sayi))
        print("Yeniden Deneyin.")