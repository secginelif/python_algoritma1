from random import choice

karakterler = ["a","b","c",1,2,3]

uzunluk =int(input("Karakter uzunluğunu giriniz: "))

sifre = ""

for i in range(uzunluk):
    sifre += str(choice(karakterler))
print("Şifreniz {} ".format(sifre))