print("OYUNCU KAYDETME PROGRAMI")

ad = input("Oyuncunun Adı: ")
soyad = input("Oyuncunun Soyadı: ")
takım = input("Oyuncunun Takımı: ")

bilgiler = [ad,soyad,takım]

print("Bilgiler Kaydediliyor ..")

print("Oyuncu Adı: {}\n Oyuncu Soyadı: {}\n Oyuncunun Takımı: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))
print("Bilgiler Kaydedildi ..")