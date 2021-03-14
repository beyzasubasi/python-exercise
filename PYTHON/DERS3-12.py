# kullanıcıdan okunan sayının kaç basamaklı olduğunu bulan algoritma

n = int(input("Bir sayı giriniz: "))
bs = 0

while(n!=0):
    n = n//10
    bs += 1

print(bs)

# n = input("Bir sayı giriniz: ")
# print(len(n))                     fonkla kısaca bulabiliriz