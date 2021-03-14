#kullanıcıdan okunan bir sayının basamaklarında bulunan en büyük rakamı bulan algoritma

n = int(input("bir sayı giriniz: "))
ebb = 0

while(n!=0):
    while(n-(n//10)*10>ebb):
        ebb = n-(n//10)*10
        n = n //10

print(ebb)