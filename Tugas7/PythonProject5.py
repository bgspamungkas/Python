def kuadrat(bil):
    hasil = []
    for a in bil:
        hasil.append(a ** 2)
    print(hasil)

bil = [2, 3, 4, 5, 6, 8, 7, 9]
print("bil  = ", bil)
print("hasil = ", end= " ")
kuadrat(bil)
