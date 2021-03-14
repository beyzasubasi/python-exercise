#for ile fibonacci yaz
#fibonacci: 1,1,2,3,5,8,13,21,34....  yeni sayı önceki iki sayının toplamıdır

a=1
b=1

fibonacci = [a,b]

for i in range(20):

    a,b = b,a+b
    fibonacci.append(b)

print(fibonacci)

#MANTIĞINI İYİ YERLEŞTİR !!!!!!!!!!!!!!



