#euler sayısını ilk 10 terimi kullanarak hesaplayan algoritma

import math
euler = 1
for n in range(1,10):   #1/10! ekleniyor
    euler += 1/math.factorial(n)
print(euler)                          #fonk ile bu şekilde yazılır
