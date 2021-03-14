''' Kullanıcının girdiği vize1,vize2,final notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.
    Vize2 toplam notun %30'una etki edecek.
    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <   55 -----> FF
'''

vize1 = int(input("Vize1 notunuzu giriniz:"))
vize2 = int(input("Vize2 notunuzu giriniz:"))
final = int(input("Final notunuzu giriniz:"))

toplamnot = (vize1*3/10) + (vize2*3/10) + (final*4/10)

if(toplamnot>=90):
    print("AA")
elif(toplamnot>=85):
    print("BA")
elif(toplamnot>=80):
    print("BB")
elif(toplamnot>=75):
    print("CB")
elif(toplamnot>=70):
    print("CC")
elif(toplamnot>=65):
    print("DC")
elif(toplamnot>=60):
    print("DD")
elif(toplamnot>=55):
    print("FD")
else:
    print("FF")
















