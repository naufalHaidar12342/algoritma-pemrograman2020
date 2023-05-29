#file drv_bil.py
import math
from bil import *
import globals
def main():
    globals.awal()
    globals.bilBulat=int(input('Masukan bilangan (+) min 2 digit :'))
    print("Panjang Bilangan : ",panjang(globals.bilBulat))
    # print("Bilangan Genap : ",is_genap(globals.bilBulat))
    # print("Jumlah Digit Genap : ",sum_genap(globals.bilBulat))
    print("Bilangan Ganjil : ",is_ganjil(globals.bilBulat))
    # print("Jumlah Digit Ganjil : ",sum_ganjil(globals.bilBulat))
    # print("Jumlah Digit Max : ",maxi(globals.bilBulat))
    # print("Jumlah Digit Min : ",mini(globals.bilBulat))
    # print("Rerata Digit : ",rerata(globals.bilBulat))
    # print("SD Digit Max : ",std_dev(globals.bilBulat))
    # print("Selisih Max-Min : ",selisih(globals.bilBulat))
    # print("Jumlah Digit : ",sum_digit(globals.bilBulat))
    # print("Apakah Bilangan Prima : ",is_prima(globals.bilBulat))
    # print("Jumlah Digit Prim
    # a : ",sum_prima(globals.bilBulat))
    # print("Bilangan Palindrom : ",is_palindrome(globals.bilBulat))
    # print("Bilangan Strong : ",is_strong(globals.bilBulat))
    # print("Bilangan Perfect : ",is_perfect(globals.bilBulat))
if __name__ == '__main__':
    main()