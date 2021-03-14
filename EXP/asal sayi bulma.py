# asal sayılar : 1e ve kendinden başka sayıya bölünmeyen
# sayı asal mı değil mi bul

print("""****************
Bir sayının asal olup olmadığını bulma

Programdan çıkmak için 'q' ya basın.
****************""")

def asalmi(sayi):

    for i in range(2,sayi):

        if (sayi % i == 0 ):
            return False

    return True



while True:
    sayi = input("Sayı:")

    if (sayi == "q"):
        print("Programdan Çıkılıyor...")
        break

    sayi = int(sayi)

    if (sayi == 1):
        print(sayi, "asal bir sayı değildir.")

    elif (sayi == 2):
        print(sayi, "asal bir sayıdır.")

    else:

        if (asalmi(sayi)):
            print(sayi,"asal bir sayıdır.")
        else:
            print(sayi,"asal bir sayı değildir.")
