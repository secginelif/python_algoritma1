def hacim_bulma():
    print("Hesaplamak istediğiniz şekli seçiniz")
    print("Kare=kare , Küre=kure Dikdörtgen prizması=dp")
    hesap = input("Hesaplamak istediğiniz şekli girin: ")

    if hesap=="kare":
        a= int(input("Bir kenar uzunluğunu giriniz: "))
        hacim = (a*a)
        return hacim

    elif hesap=="kure":
        r= int(input("Kürenin yarı çapını giriniz: "))
        hacim = (4/3 )* (3.14) * (r**3)
        return hacim

    elif hesap=="dp":
        a=int(input("Kısa kenarı giriniz: "))
        b=int(input("Uzun kenarı giriniz: "))
        c=int(input("Yüksekliği giriniz: "))
        hacim= (a*b*c)
        return hacim
    else:
        print("Doğru şekil yazınız.")

while True:
    print(hacim_bulma())
    break