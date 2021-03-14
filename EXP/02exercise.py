#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m)*Boy(m)

k = int(input("Kilonuz:"))
b = float(input("Boyunuz:"))

bki = k/(b**2)
print("Beden Kitle İndeksiniz:", bki)



#boy = float(input("Boy:"))
#kilo = int(input("Kilo:"))

#print("Beden Kitle İndeksi:",kilo / (boy ** 2))

#çıktı
#Boy:1.73
#Kilo:84
#Beden Kitle İndeksi: 28.06642386982525