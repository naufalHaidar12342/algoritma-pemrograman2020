import os,sys

# def main():
#     f='Hello Algoritma dan Pemrograman'
#     nama=input("masukkan nama=")
#     nilai=float(input("nilai="))
#     sks=int(input("sks="))
#     if nilai>=75 and sks>=144:
#         lulus=True
#     if nilai<75 and sks<144:
#         lulus=False
#     print(f)
#     print("Nama=",nama,"Nilai=",nilai,"SKS=",sks,"Lulus=",lulus)
    
# if __name__ == "__main__":
#     main()


def main1():
    f='Hello Algoritma dan Pemrograman'
    nama=input("nama\t:")
    nilai=float(input("nilai\t:"))
    sks=int(input("sks\t:"))
    lulus=bool(input("Lulus\t:"))
    print(nama+',bernilai' + str(nilai) + 'dengan jumlah sks' + str(sks)+'dan status kelulusan' + str(lulus))
    print(nama,',bernilai' ,nilai,'dengan jumlah sks' ,sks, 'dan status kelulusan' ,lulus)
    # if nilai>=75 and sks>=144:
    #     lulus=True
    # if nilai<75 and sks<144:
    #     lulus=False
    # print(f)
    # print("Nama=",nama,"Nilai=",nilai,"SKS=",sks,"Lulus=",lulus)
    
if __name__ == "__main__":
    main1()