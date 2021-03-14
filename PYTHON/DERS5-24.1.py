


x = input("Sayilarinizi giriniz : ")
dizi = x.split()
eb = 0
ek= int(dizi[0])
toplam =0

for sayi in dizi:
    sayi=int(sayi)
    toplam+=sayi
    if sayi>eb:
        eb=sayi
    if sayi<ek:
        ek=sayi

ort = toplam/len(dizi)

print("En Büyük sayi: " ,eb)
print("En küçük sayi: ",ek)
print("Ort: ",ort)