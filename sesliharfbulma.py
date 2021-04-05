sesliharf = "aeıiöouü"

isim = input("İsminizi yazın :")

sesli_sayi = 0
for i in isim:
    if i in sesliharf:
        sesli_sayi += 1
print("Sesli harf sayısı :",sesli_sayi)       
print("Sessiz harf sayısı :",len(isim)-sesli_sayi)
