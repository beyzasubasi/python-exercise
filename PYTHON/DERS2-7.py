#1 den(dahil) p ye(dahil) kadar olan tek sayıların toplamını bulan algoritma

p = int(input("p değerini giriniz: "))
toplam = 0

for n in range(1,p+1,2):
    toplam = toplam + n
print(toplam)

