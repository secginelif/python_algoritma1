#vizenin %40 finalin %60 ortalama 50den büyükse geçti küçükse kaldı

vize = int(input("Vize notu :"))
final = int(input("final notu :"))
ortalama = vize * 0.4 + final * 0.6
print("Ortalama :",ortalama)

if ortalama>=50 :
    print("Geçti...")
else:
    print("Geçemedi...")