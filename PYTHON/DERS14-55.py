#

from fonksiyon import divisors

liste = []
toplamlar = set()

for n in range(11,28123): #en küçük abundant sayısı 12 dendiği için 11den başladım
    if(sum(divisors(n))>n): #bölenlerinin toplamı sayının kendisinden daha büyükse
        liste.append(n) #listeye ekledim (abundat sayıları olulturan liste)

for p in liste:
    for q in liste:
        if(p+q<28123): #toplamları 28123ten büyük olanların 2 abundat sayının toplamı olarak yazıldığın söylenmitşi
            toplamlar.add(p+q) #(abundat sayıların üzerinde gezerek p ve q ların toplamını başka listeye atıyorum)

sayilar = set(range(1,28123))

print(sum(sayilar-toplamlar))
