#PC 1 ile 100 arasındaki bir sayıyı rastgele belirlesin ve oyuncu bunu tahmin ederek bulmaya çalışsın

import random

sayi = random.randint(1,100)
tahmin, deneme = 0, 0

while(tahmin!=sayi):
    tahmin = int(input("tahmininiz nedir: "))
    deneme += 1

    if(tahmin>sayi):
        print("Daha büyük bir tahminde bulundunuz..")

    else:
        print("Daha küçük bir tahminde bulundunuz..")

print("Bildiniz..\nKaçıncı denemede buldunuz: ", deneme)

