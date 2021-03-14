"""
kullanıcıdan 3 basamaklı bir sayı okuyup sayının bas tersten yazılımı ile
elde edilecek sayının okunan sayıya eşit olup olmadığını kontrol eden bir algo
ÖRN: girdi 575 ise algo "eşit" çıktısını, 134 olduğunda ise "eşit değil" çıktısını vermelidir
"""

sayi=int(input("3 Basamaklı Bir Sayi Giriniz: "))

a=sayi%10   #birler
b=sayi//10
b=b%10      #onlar
c=sayi//100 #yüzler

ters=100*c+10*b+c

if(sayi==ters):
    print("Tersi Birbirine Eşittir!")

else:
    print("Eşit Değildir!")



