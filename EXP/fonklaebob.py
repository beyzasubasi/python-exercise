#Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
# iki sayının en büyük ortak bölenini bulmalıyız.

def ebobbul(sayi1,sayi2):
    i=1
    ebob=1


    while (i<=sayi1  and  i<=sayi2):

        if(not(sayi1 % i)  and  not(sayi2 % i)):
            ebob = i
        i+=1
    return ebob


sayi1 = int(input("sayi1 giriniz:"))
sayi2 = int(input("sayi2 giriniz:"))


print("EBOB:",ebobbul(sayi1,sayi2))


