jumlah = int(input('Masukkan nilai :'))
bil = []
for b in range(jumlah):
    angka = int(input('Masukkan data: '))
    bil = bil + [angka]
bil.sort(reverse=True)
print(bil)
