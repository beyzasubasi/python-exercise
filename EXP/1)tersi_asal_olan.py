"""
hem kendisi hem de ters yazılışı birer asal sayı olan sayılara emirp sayıları denir
(13 ve onun tersten yazılışı 31, 37 ve onun tersten yazılışı 73 birer asal sayıdır)
1 milyondan küçük kaç emirp saysı olduğunu çıktı veren algo
(ihtiyaç dahilinde sayı asal ise 1, değilse 0 döndüren isprime fonk veya
bir sayıdan küçük bütün asal sayıları bir liste olarak döndüren allprimes fonk kullanabilirsiniz)
"""

n = int(input("hangi sayıya kadar olan asal sayılar hesaplansın: "))
def allprimes(n):
    primes = list(range(2,n+1,1))
    for x in range(0,int(n/2)+1):
        if(primes[x]!=0):
            for i in range(x+primes[x],n-1,primes[x]):
                primes[i]=0
    primes.sort()
    return(primes[primes.count(0):])

"""
def isprime(n):
    i = 3
    if(n<2):
        return(0)
    if(n!=2 and n%2==0):
        return(0)
    while(i<=n**(1/2)):
        if(n%i==0):
            return(0)
        i += 2
    return(1)
"""