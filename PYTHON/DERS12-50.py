#bir sayının bas. faktöriyellerinin toplamı kendisine eşit olan sayıların toplamı
#1 ve 2 dahil değil

from math import factorial
sonuc = 0
for n in range(3,100000):    #neden 100.000
    toplam = 0
    for i in str(n):
        toplam += factorial(int(i))
    if(n==toplam):
        sonuc += n
        print(n)
print(sonuc)
