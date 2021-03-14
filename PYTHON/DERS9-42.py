#10000den küçük arkadaş sayıların bölenlerinin toplamını bulan algoritma

def d(p):          #bölenlerin toplamını veriyor
    toplam = 1
    for n in range(2, p//2+1):  # n in yarısına kadar olan sayılara bölünüp bölünmediğini konrtol ediyorum
        if(p//n*n==p):          #sonra bölenlerinin toplmını buluyorum
            toplam += n
    return(toplam)

gtoplam = 0

for m in range(2,10000):  #
    s = d(m)  #s değeri min bölenlerinin toplamına eşit olsun

    if(m==s):  #sayılsr birbirin eşit olmamalıydı olursa fordan çıkacak
        continue

    if(s>10000): #m in bölenlerinin toplamı olan s 10.000den büyükse de koşul gerçekleşmediği için contintue ile çıkılır
        continue
                  # m in bölenlerinin toplamının tekrar bölenlerinin toplamını bulup [ d(s) ] eşitliği sağlatıyorum
    if(m==d(s)):  #m in kendisi s in bölenleriin toplamına eşitse bunlar arakadsaş sayılardır diyip
        gtoplam += m  #m i gtoplama ekle dedim

print(gtoplam)
