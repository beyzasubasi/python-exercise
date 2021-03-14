# kullanıcı girişi yaz fakat 3 hakla sınırlı olsun


KA = "beyzi"
KŞ = "123456789"
denemehakkı = 3


while True:


    kullanıcıadı = input("Kullanıcı Adınızı Giriniz:")
    kullanıcışifre = int(input("Şifrenizi Giriniz:"))


    if(kullanıcıadı == KA and kullanıcışifre != KŞ):
        print("Şifre hatalı..")
        denemehakkı -=1

    elif(kullanıcıadı != KA and kullanıcışifre == KŞ):
        print("Kullanıcı adı hatalı..")
        denemehakkı -=1

    elif(kullanıcıadı != KA and kullanıcışifre != KŞ):
        print("Kullanıcı adı ve şifre hatalı..")
        denemehakkı -=1

    else:
        print("Giriş başarılı!")
        break

    if(denemehakkı==0):
        print("Deneme hakkınız bitti..")
        break