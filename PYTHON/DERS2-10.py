# 10 binden küçük fibonacci sayılarının en büyüğünü bulan algoritma

fn1, fn2 = 1, 1
fn3 = 42         #fn3 e herhangi bir değer atamamız gerekiyordu tanımlı olması için

while(fn3<10000): #10.000den küçük olduğu yerlerde yaptırmak istediğimiz işlemleri döngüye aldık

    fn3 = fn1 + fn2
    fn1 = fn2
    fn2 = fn3

print(fn1)      #fn3 ü  fn2 ye, fn2 yi fn1 e atadığımız için fn1 i yazdırdık

