# p! hesaplayan algoritma

p = int(input("p yi giriniz: "))
faktoriyel = 1

for n in range(1,p+1):           #kısa yol olarak hoca aşağıdaki gibi yazmış
    faktoriyel = faktoriyel*n

    if(n==p):                   #mesela p+1de bitmesi demek n==p demek
        print(faktoriyel)       #algo yazarken bi nevi for u tanımlamış olduk aslında

    else:                       #bu işi zaten for yapıyor yani ben boşuna
        n = n+1                 #aynısını tekrar yazmış oluyorum

#for n in range(1,p+1):
#    faktoriyel = faktoriyel*n
#print(faktoriyel)