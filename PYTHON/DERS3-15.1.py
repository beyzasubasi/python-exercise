#euler sayısını ilk 10 terimi kullanarak hesaplayan algoritma

euler=2
p=2
faktoriyel=1

while(p<10):
    faktoriyel = faktoriyel*p
    euler = euler + 1/faktoriyel
    p+=1

print(euler)