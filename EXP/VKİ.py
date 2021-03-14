#Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.
#Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)
#BKİ 18.5'un altındaysa -------> Zayıf
#BKİ 18.5 ile 25 arasındaysa ------> Normal
#BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu
#BKİ 30'un üstündeyse -------------> Obez


boy = float(input("Boyunuzu Giriniz:"))
kilo = int(input("Kilonuzu Giriniz:"))

BKİ = kilo/(boy*boy)

print("Beden Kitle İndeksiniz:",BKİ)

if (BKİ<18.5):
    print("Zayıfsın dewamke")

elif (BKİ>=18.5 and BKİ<25):
    print("It's normal bro")

elif (BKİ>=25 and BKİ<30):
    print("Fazla kilolusun gardaşım")

#elif(BKİ>=30):
else:
    print("Obezsin az ye..")