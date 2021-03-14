# 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.
# (a <= 100,b <= 100)


def pisagorbul():

    pisagorlistesi = list()

    for i in range(1, 101):

        for j in range(1, 101):

            c = (i ** 2 + j ** 2) ** 0.5

            if (c == int(c)):

                pisagorlistesi.append((i, j, int(c)))

    return pisagorlistesi


for i in pisagorbul():          # neden gerek var bunu yazmaya??????????????
    print(i)