#kullanıcıdan 2 sayı okuyup bunlardan büyük olanı çıktı veren algo

sayi1 = int(input("sayi1 girin: ")) #int şeklinde belirttiğim için if in içine int yerleştirmeme gerek kalmadı
sayi2 = int(input("sayi2 girin: ")) #hiçbir yere int yazmasaydım küsuratlı sayılar ve harfler için de program çalışacaktı

# if(sayi1>sayi2):
#    print(sayi1)

#if(sayi2>=sayi1):
#    print(sayi2)       bu şekilde tek değeri 2 koşulla sağlatarak uzatmaya gerek yok

if(sayi1>sayi2):
    print(sayi1)

else:
    print(sayi2)


