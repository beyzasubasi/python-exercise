#bir sayının tam bölenlerini bulma

print("""****************
Bir sayının bölenlerini bulma

Programdan çıkmak için 'q' ya basın.
****************""")


def tambolenleribul(sayi):
    tambolenlistesi = []

    for i in range(1,sayi+1):

        if (sayi % i == 0):
            tambolenlistesi.append(i)

    return tambolenlistesi

while True:

    sayi = input("Sayı:")

    if (sayi == "q"):
        print("Programdan Çıkılıyor...")
        break
    else:
        sayi = int(sayi)
        print("Tam Bölenler:",tambolenleribul(sayi))

