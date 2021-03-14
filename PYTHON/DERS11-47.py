# a**b   2 <= a <= 100 kaç farklı ifade olacağını veren algoritma
#        2 <= b <= 100

kuvvet = set()
for a in range(2,101):
    for b in range(2,101):
        kuvvet.add(a**b)
print(len(kuvvet))
