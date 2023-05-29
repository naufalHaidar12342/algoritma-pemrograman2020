#file drv_bil.py
import math
from bil import *
import globals
def main():
    globals.awal()
    globals.bilBulat=int(input('Masukan bilangan (+) min 2 digit :'))
    print('Panjang Bilangan : ',panjang(globals.bilBulat))
    print('Bilangan Genap : ',isGenap(globals.bilBulat))
    print("Jumlah Digit Genap : ",sumGenap(globals.bilBulat))
    print("Bilangan Ganjil : ",isGanjil(globals.bilBulat))
    print("Jumlah Digit Ganjil : ",sumGanjil(globals.bilBulat))
    print("Jumlah Digit Max : ",maxi(globals.bilBulat))
    print("Jumlah Digit Min : ",mini(globals.bilBulat))
    print("Rerata Digit : ",rerata(globals.bilBulat))
    print("SD Digit Max : ",std_dev(globals.bilBulat))
    print("Selisih Max-Min : ",selisih(globals.bilBulat))
    print("Jumlah Digit : ",sunDigit(globals.bilBulat))
    print("Apakah Bilangan Prima : ",isPrima(globals.bilBulat))
    print("Jumlah Digit Prima : ",sumPrima(globals.bilBulat))
    print("Bilangan Palindrom : ",palindrome(globals.bilBulat))
    print("Bilangan Strong : ",strong(globals.bilBulat))
    print("Bilangan Perfect : ",perfect(globals.bilBulat))
if __name__ == '__main__':
    main()