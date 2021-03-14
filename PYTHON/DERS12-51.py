#

sayac = 0
for n in range(2,100000):  #100000 olmasının sebebi 678910.sunu soruyor
    if(str(2**n)[:3]=="123"):
        sayac += 1
        print(sayac, n)
