# kullanıcıdan okunan sayının tek sayı mı çift sayı mı olduğunu çıktı veren algo

n = int(input("bir sayı giriniz: "))

if((n//2)*2 == n):         # (TAM(n/2)*2=n) algoritma yazarken tam sayı bölmesini bu şekilde dile getiriyoruz
    print("Çift Sayıdır!") # kod yazarken // ifadesi tam sayı bölmesini ifade eder

else:
    print("Tek Sayıdır!")