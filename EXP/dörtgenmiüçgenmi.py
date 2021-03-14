'''
Şimdi de geometrik şekil hesaplama işlemi yapalım.
İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.
Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen
mi olduğunu bulmaya çalışın.
Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi
olduğunu bulmaya çalışın.
Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.
Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.
Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak.
Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu
kullanabilirsiniz.
Kullanımı şu şekildedir ;

abs(-4)                      abs(5)
4                            5                             '''

seçim = input("Üçgeni tercih ediyorsanız Ü girin.\nDörtgeni tercih ediyorsanız D girin\n")

if(seçim == "Ü" ):
    print("Üçgeni seçtiniz")

    k1 = int(input("1.Kenar:"))
    k2 = int(input("2.Kenar:"))
    k3 = int(input("3.Kenar:"))


    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a): #üçgen olma şartı

        if((k1==k2 and k1!=k3) or (k1==k3 and k1!=k2) or (k2==k3 and k2!=k1)):
            print("İkizkenar üçgen")

        elif(k1==k2==k3):
            print("Eşkenar üçgen")

        else:
            print("Çeşitkenar üçgen")
    else:
        print("Üçgen belirtmiyor..")


elif(seçim == "D" ):
    print("Dörtgeni seçtiniz")

    d1 = int(input("1.Kenar:"))
    d2 = int(input("2.Kenar:"))
    d3 = int(input("3.Kenar:"))
    d4 = int(input("4.Kenar:"))


    if(d1==d2 and d1==d3 and d2==d4):
        print("Kare")

    elif( d1==d3 and d2==d4  ):
        print("Dikdörtgen")

    else:
        print("Dörtgen")

else:
    print("Geçersiz Seçim!")

