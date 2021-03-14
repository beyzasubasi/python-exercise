#for döngüsüyle sayının faktoriyelini bulma
#çıkmak için q ya basınız



while True:

    fak = input("Faktöriyelini istediğiniz sayıyı giriniz:")


    if(fak=="q"):
        print("Program soınlandırılıyor..")
        break

    else:

        faktöriyel = 1
        fak = int(fak)

        for i in range(fak,0,-1):
            faktöriyel*=i
        print("Faktöriyel",faktöriyel)

