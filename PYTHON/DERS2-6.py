#1den 100e kadar olan sayıların toplamını bulan algoritma

toplam = 0

for n in range(1,101):   #son değeri dahil etmediği için 101 aldım
    toplam = toplam + n  #sağ tarafa yazılan şeylerin kesinlikle daha önceden tanımalnamış olması
                         #ya da bir değer ataması yapılmış olması gerekiyor
print(toplam)