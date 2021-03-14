"""
bir kitaba sayfa numaraları verilirken 689 tane 1 rakamı kullanılmıştır
bu kitabın sayfa sayısını bulunuz

"""
toplam=0
for i in range(1,2000):
    sayfa_no=list(str(i))

    for j in sayfa_no:
        if(str(j)=="1"):
            toplam+=1

        if(toplam==689):
            print("sayfa sayisi:",i)
            break