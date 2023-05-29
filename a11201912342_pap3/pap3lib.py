import pap3global

def faktorPrima(n):
    list1=[]
    loop=2
    while loop<=n:
        if n%loop==0:
            n/=loop
            list1.append(loop)
        else:
            loop+=1
    return list1

def faktorUmum(a,b):
    if 0<a<=b:
        listA=faktorPrima(a)
        listB=faktorPrima(b)
        list2=[]
        for angka1 in range(0,len(listA)):
            for angka2 in range(0,len(listB)):
                if listA[angka1]==listB[angka2]:
                    listB.remove(listA[angka1])
                    list2.append(listA[angka1])
                    break
    if 0<b<=a:
        listA=faktorPrima(a)
        listB=faktorPrima(b)
        list2=[]
        for angka1 in range(0,len(listB)):
            for angka2 in range(0,len(listA)):
                if listB[angka1]==listA[angka2]:
                    listA.remove(listB[angka1])
                    list2.append(listA[angka2])
                    break
    return list2
    # ubah_list=set(list2)
    # balik_list=list(ubah_list)
    # list_3=[]
    # for x in balik_list:
    #     list_3.append(x)
    # return list_3
    # list2=[]
    # listA=[2,2,3,3]
    # listB=[2,2,2,3,3]
    # for angka1 in listA[x]:
    #     for angka2 in listB[y]:
    #         if angka1==angka2:
    #             list2.append(angka1)    
    # return list2

def fpb(a,b,hasil):
    hasil=pap3global.data_int
    list_X=faktorUmum(a,b)
    for kali in range(0,len(list_X[kali])):
        kali2=list_X[kali]*list_X[kali]
        hasil.append(kali2)
    return hasil

    
def selisih(w1,w2,w3):
    p1=d%60
    p2=d//60
    p3=p2%60
    p4=p2//60
        
# listFaktorUmum=[]
# listFaktorUmum=faktorUmum(a,b)
# pap3global.data_int=max(listFaktorUmum)
# hasil=pap3global.data_int
    
