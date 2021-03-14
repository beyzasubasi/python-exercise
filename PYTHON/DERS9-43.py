#sıralama algoritması (bubble sort horon tepen video)

#a = [200, 3, 511, 72, 11, 13, 17, 19, 23, 249, 31, 37, 41, 43, 47]

#for j in range(len(a)-1):
#    for i in range(len(a)-1):
#        if(a[i]>a[i+1]):
#            a[i], a[i+1] = a[i+1], a[i]
#print(a)

#ilk sıralamada en büyük değer herzaman en sağa yerleşir
#en sondaki ve bir önceki eleman sadece ilk turda karşılaştırılmalı
#bu ifadeyi sadelştirmemiz lazım
#dene! (bubble sort)

a = [200, 3, 511, 72, 11, 13, 17, 19, 23, 249, 31, 37, 41, 43, 47]

j = 0
sure = len(a)-1
degistimi = 1

while(j<sure and degistimi==1):
    degistimi = 0
    soneleman = a[sure]
    for i in range(len(a)-1):
        if(a[i]>a[i+1]):
            a[i], a[i+1] = a[i+1], a[i]
            degistimi = 1
    sure = sure - 1
    j +=1
print(a)
