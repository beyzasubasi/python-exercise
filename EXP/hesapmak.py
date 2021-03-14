# hesap makinesi

print("*** HESAP MAKİNESİ ***")

a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))

print("İşlem 1: Toplama\nİşlem 2: Çıkarma\nİşlem 3: Çarpma\nİşlem 4: Bölme")

islem = int(input("Yapmak İstediğiniz İşlemi Seçiniz:"))


if islem == 1:
    print("{} + {} = {}".format(a,b,a+b))

elif islem == 2:
    print("{} - {} = {}".format(a,b,a-b))

elif islem == 3:
    print("{} * {} = {}".format(a,b,a*b))

elif islem == 4:
    print("{} / {} = {}".format(a,b,a/b))

else:
    print("Geçerli bir işlem seçiniz..")
