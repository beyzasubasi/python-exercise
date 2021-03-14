#kullanıcıdan okunan sayının basamakları toplamını bulan algoritma

n = int(input("Bir sayı giriniz: "))
bt = 0

while(n!=0):

    bt += n-(n//10)*10
    n = n // 10          #sayı 1234 iken bu satırda 123 yapılıyor
                         #bi sonrakinde 12 şeklinde küçülerek gitmesini sağlar
print(bt)