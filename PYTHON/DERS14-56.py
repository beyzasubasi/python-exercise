#

def ispalindrome(n):
    if(str(n)==str(n)[::-1]): #sayının kendisi tersten yazılışına eşitse bize 1 döndürsün
        return(1)
    else:
        return(0)  #değilse 0 döndürsün

lychrel = 0

for m in range(1,10000):
    n = m
    for i in range(50):
        if(ispalindrome(n+int(str(n)[::-1]))==1): # n i str dönüştürüp ayna görüntüsünü aldım ve intliyorum eğer 1se
            break
        else:
            n += int(str(n)[::-1])  #n i ayna görüntüsüyle toplayıp tekrar yukarı gönderiyorum
    else:
        lychrel += 1   # ve ni 50 defa kendi ayna görüntüsüyle toplayıp bir palindrom elde edemediysem
print(lychrel) # o zaman bu bir lychrel sayısıdır
