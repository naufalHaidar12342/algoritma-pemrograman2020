def cmToM(c):
    # c=int(input("angka="))
    cm=c%100
    m=c//100
    return tuple([m,cm])

def hariToTahun(hari):
    totalhari=hari-365
    tahun=totalhari/365
    bulan=totalhari//30
    hari_s=totalhari(bulan*30)
    return tuple([hari_s,bulan,tahun])

def generator(n):
    lst=[]
    sementara=n
    lst.append(sementara)
    while sementara>1:
        if n%2==0:
            x=n/2
            lst.append(x)
        if n%2!=0:
            y=(3*n)+1
            lst.append(y)
    return lst 

