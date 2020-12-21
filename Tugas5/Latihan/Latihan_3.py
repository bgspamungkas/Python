def faktorial(n):
    faktorialn = 1
    while( n > 0):
        faktorialn = faktorialn * n
        n -= 1
    return faktorialn
def kombinasi( a , b ):
    c = a - b
    hasil = faktorial(a) / (faktorial(b) * faktorial(c))
    print(hasil)
def permutasi( a , b ):
    c = a - b
    hasil = faktorial(a) / faktorial(c)
    print(hasil)

print('a')
a=5
b=3
kombinasi(a,b)

print('b')
x=10
y=7
permutasi(x,y)
