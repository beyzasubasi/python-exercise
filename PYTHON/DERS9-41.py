#p sayısının bölenlerinin toplamını veren algoritma

p = int(input("bir sayı girin: "))
toplam = 1

for n in range(2, p//2+1):

    if(p//n*n==p):
        toplam += n

print(toplam)
