#1**2 + 2**2 + 3**3 + .. + 1000**1000 = toplamının son 10 basamağını veren algo

toplam = 0

for i in range(1,1001):
    toplam += i**i

#print(len(str(toplam)))   str ye çevirirsem kaç basamaklı olduğunu bulabilirim

print(str(toplam)[-10:])    #sondan 10 basamağını yazdırmamızı söylüyoruz
