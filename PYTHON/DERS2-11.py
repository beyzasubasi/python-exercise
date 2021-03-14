# p sayısının bölenlerini bulan algoritma(1 ve kendisi hariç)

p = int(input("Bölenlerini bulmak istediğiniz sayıyı giriniz: "))

for n in range(2, p//2+1):
    if((p//n)*n == p):
        print(n)
