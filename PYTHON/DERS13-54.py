#

dosya=open("p067_triangle.txt")
ucgen = []

for line in dosya.readlines(): #dosyanın içindeki her satır için bu işlemleri yap
    line = line.rstrip('\n').split(' ') #satır sonu karakterini çıkardım ve elemanları boşlukla ayırdım
    ucgen.append(line)   #her bir satırı üçgen listesine ekledim
dosya.close()             #dosyayı okudum kapatıyorum

for n in range(len(ucgen)-2,-1,-1):
    for m in range(len(ucgen[n])):
        ucgen[n][m] = int(ucgen[n][m]) +  max(int(ucgen[n+1][m]),int(ucgen[n+1][m+1]))

print(ucgen[0][0])
