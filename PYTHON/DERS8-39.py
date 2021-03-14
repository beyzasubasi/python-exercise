#biz 10 ile 100arasında bir sayıyı rastgele belirleyelim, pc bunu tahminle bulmaya çalışsın, bizden alacağı 1 cevabının tahminin daha büyük olduğunu
#-1 cevabının daha küçük olduğunu ve 0 cevabının da bildiğini söyleyelim

alt = 1
ust = 100
sonuc = 42   #gireceğim 0 1 -1 değerlerini tuttuğum değişken

while(sonuc!=0):

    tahmin = (alt + ust) // 2
    print("Tahmin Edilen Sayı:",tahmin)

    sonuc = int(input("Tahmin durumu nedir: "))

    if(sonuc==1):
        ust = tahmin

    elif(sonuc==-1):
        alt = tahmin

print("Oyun Bitti..")
