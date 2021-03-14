#Kodlama egzersizimizde bir sınıfın harf notlarını hesapladığımız programı geliştirerek kalanları "kalanlar.txt"
# dosyasında ve geçenleri "geçenler.txt" dosyasına yazmaya çalışın.

def not_hesaplama(satır):
    satır = satır[:-1]  # satırlarımızın sonunda görünmeyen \n var bunu yaptığımızda \n i silmiş oluyoruz
    liste = satır.split(",")  # split fonk satırları birbirinden ayırmamızı sağlar liste şeklinde sıralattık
    # print(liste)       ['Hatice Günday', '70', '90', '20']
    #  ['Mustafa Akyürek', '90', '80', '60']
    # ['Ramazan Topaloğlu', '60', '30', '50']

    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    ort = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)

    if (ort >= 90):
        harf = "AA"
    elif (ort >= 85):
        harf = "BA"
    elif (ort >= 80):
        harf = "BB"
    elif (ort >= 75):
        harf = "CB"
    elif (ort >= 70):
        harf = "CC"
    elif (ort >= 65):
        harf = "DC"
    elif (ort >= 60):
        harf = "DD"
    elif (ort >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + " ---> " + harf + "\n"


with open("dosya.txt", "r", encoding="utf-8")as file:
    eklenecekler_list = []

    for i in file:
        eklenecekler_list.append(not_hesaplama(i))

    with open("notlar.txt", "w", encoding="utf-8") as file2:
        for i in eklenecekler_list:
            file2.write(i)
