#Kapı arkası hediye oyunu

import random

hediye = random.randint(1,10)

tercih = int(input("tercihiniz nedir: "))

while(hediye==tercih):
    tercih = random.randint(1,10)

print(hediye, tercih)
karar = int(input("son kararınız nedir: "))

if(karar==hediye):
    print("kazandınız")
else:
    print("kaybettiniz")
