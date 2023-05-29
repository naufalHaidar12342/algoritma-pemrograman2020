import globals

def panjang(n):
    sementara=n
    count=0
    while sementara!=0:
        digitnya=sementara%10
        count+=1
        sementara=sementara//10
    return count
def is_ganjil(n):
    if n%3==0:    
# def is_genap(n):
#     'adalah'
# def sum_ganjil(n):      
# def sum_genap(n):    
# def sum_digit(n):    
# def maxi(n):    
# def mini(n):    
# def rerata(n):    
# def varian(n):    
# def std_dev(n):    
# def selisih(n):
# def is_prima(n):
# def sum_prima(n):
# def is_palindrome(n):
# def is_strong(num):
# def is_perfect(n):
