import pap3global
from pap3lib import *


def main():
    pap3global.initAll()
    print(faktorPrima(315))
    # print(faktorUmum(54,24))
    print(fpb(36,48,pap3global.data_int))

if __name__ == "__main__":
    main()