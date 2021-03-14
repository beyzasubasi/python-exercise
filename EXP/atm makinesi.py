''' ATM MAKİNESİNE HOŞGELDİNİZ

İşlemler:
1.Bakiye sorgulama
2.Para yatırma
3.Para çekme

programdan çıkmak için 'q' ya basın
'''

print("İşlemler:\n\n1.Bakiye sorgulama\n2.Para yatırma\n3.Para çekme\n\nProgramdan çıkmak için 'q' ya basın\n\n")


bakiye = 1000

while True:

    işlem = input("\nİşlem seçiniz:")     # int(input()) girmedik çünkü kullanıcıya q ya girmesini de belirttik int alsaydk sadece sayı girilmesi
                                          # isteneceğinden q da hata verirdi bu şekilde de str old için işlem numaralarını "" içinde str olarak istedik
    if(işlem == "q"):
        print("Yine Bekleriz..")
        break



    elif(işlem=="1"):

        print("Bakiye Sorgulama")
        print("Mevcut Bakiyeniz:{}tl".format(bakiye))



    elif(işlem=="2"):

        print("Para Yatırma")
        YT = int(input("Yatırılacak Tutarı Giriniz:"))

        print("Paranız Yatırılıyor..")
        bakiye += YT
        print("Mevcut Bakiyeniz:{} tl".format(bakiye))



    elif(işlem=="3"):

        print("Para Çekme")
        ÇT = int(input("Çekilecek Tutarı Giriniz:"))

        if(ÇT>bakiye):
            print("Yetersiz Bakiye!")
            continue

        print("Paranız Çekiliyor..")
        bakiye -=ÇT
        print("Mevcut Bakiyeniz:{}tl ".format(bakiye))




    else:
        print("Geçersiz İşlem!")
