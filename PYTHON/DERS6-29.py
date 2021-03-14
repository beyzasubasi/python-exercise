# p sayısının kaç böleni old çıktı veren algo

p = int(input("bir sayı girin: "))
bs = 2
for n in range(2, p//2+1):
    if(p//n*n==p):
        bs += 1
print(bs)