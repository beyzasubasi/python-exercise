#basamaklarındaki rakamların 5.kuvveti şeklinde yazılabilen tüm sayıların toplamı

toplam = 0
for i in range(1000,354294): # max 6bas kadar bakabileceğimiz için
    kontrol = 0              # 6*9**5 = 354294
    for j in str(i):
        kontrol += int(j)**5
    if(i==kontrol):
        toplam += kontrol
print(toplam)
