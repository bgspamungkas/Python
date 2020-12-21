def dataStat(x):
    jumlah = sum(x)
    bagi = len(x)
    a = jumlah/bagi
    b = max(x)
    c = min(x)
    return(a, b, c)

bil = (7, 8, 9, 5, 2, 1, 14, 16, 11)
print('(rata-rata, nilai tertinggi, nilai terendah)')
print(dataStat(bil))
    
