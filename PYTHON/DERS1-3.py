#kullanıcıdan 3 sayı okuyup en büyüğünü çıktı veren algoritma

sayi1 = int(input("sayi1 girin: "))
sayi2 = int(input("sayi2 girin: "))
sayi3 = int(input("sayi3 girin: "))

ebs = sayi1

if(sayi2>ebs):
    ebs = sayi2
if(sayi3>ebs):
    ebs = sayi3

print(ebs)