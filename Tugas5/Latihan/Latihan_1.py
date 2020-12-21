def isPythagoras (a,b,c):
    if((a * a) == ( c * c )-( b * b )
       or ( b * b ) == ( c * c )-( a * a )
       or ( c * c ) == ( a * a )+( b * b )):
        print(True)
    else:
        print(False)


print('a')
isPythagoras(3,4,5)

print('b')
isPythagoras(5,9,12)

print('c')
isPythagoras(8,6,10)

print('d')
isPythagoras(7,8,11)
