import globals

def panjang(n):
    str_inp=str(globals.bilBulat)
    return len(str_inp) 

def is_ganjil(n):
    cek_ganjil=globals.bilBulat
    for i in range(1,cek_ganjil):
        if i%2!=0:
            checks=True
        else:
            checks=False
    return checks

# def is_genap(n):
#     cek_genap=int(globals.bilBulat)
#     for genap in range(cek_genap):
#         if cek_genap%2==0:
#             checks=True
#         else:
#             checks=False
#     return checks

# def sum_genap(n):
    

# def sum_ganjil(n):
#     is_ganjil(n)
#     jumlahGanjil=[]
#     cetak=[]
#     jumlahGanjil.append(is_genap(n))
#     for angka in jumlahGanjil:
#         cetak.append(angka)
#     return cetak

# def sum_digit(n):
#     count=0
#     list1=[]
#     list1.append(n)
#     for angka in list1:
#         count+=1
# def maxi(n):
#     maks=0
#     list1=[]
#     list1.append(globals.bilBulat)
#     for angka in list1:
#         if maks<angka:
#             maks=angka
#     return maks
    

#  def max(arr, max_=None):
#     if max_ is None:
#         max_ = arr.pop() 
#         current = arr.pop()
#     if current > max_:
#          max_ = current
#     if arr:
#         return max(arr, max_)
#     return max_    
#  def mini(n):    
#  def rerata(n):    
#  def varian(n):    
#  def std_dev(n):    
#  def selisih(n):
#  def is_prima(n):
#  def sum_prima(n):
#  def is_palindrome(n):
#  def is_strong(num):
#  def is_perfect(n):
  
