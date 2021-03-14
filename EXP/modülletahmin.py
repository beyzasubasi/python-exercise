
import random       #rastgele sayı seçimi için modül
import time         #programın beklemesi için modül


print("SAYI TAHMİN OYUNU\n 1 ile 40 arasında sayıyı tahmin edin")

rastgelesayi = random.randint(1,40)    #randint fonk rastgele sayi uretir
tahminhakki = 7


while True:

    tahmin = int(input("Tahmininiz:"))

    if(tahmin < rastgelesayi):
        print("Bilgiler sorgulanıyor..")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyin")
        tahminhakki -=1

    elif(tahmin > rastgelesayi):
        print("Bilgiler sorgulanıyor..")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyin")
        tahminhakki -=1

    else:
        print("Bilgiler sorgulanıyor..")
        time.sleep(1)
        print("Tebrikler! Sayımız:",rastgelesayi)
        break

    if(tahminhakki == 0):
        print("Tahmin hakkınız bitti..")
        print("Sayımız:",rastgelesayi)
        break
