# kullanıcı adı şifre uyumu


kullanıcıadım = "beyzi"
kullanıcışifrem = "123456789"


KA = input("kullanıcı adı:")
KŞ = input("kullanıcı şifresi:")


if(kullanıcıadım == KA and kullanıcışifrem != KŞ):
    print("kullanıcı adınız doğru fakat şifreniz yanlış")

elif(kullanıcıadım != KA and kullanıcışifrem == KŞ):
    print("kullanıcı adınız yanlış fakat şifreniz doğru")

elif(kullanıcıadım != KA and kullanıcışifrem != KŞ):
    print("kullanıcı adınız ve şifreniz yanlış")
else:
    print("Giriş başarılı ..")