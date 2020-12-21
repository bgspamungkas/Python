print('------------------------------------------')
print('        PROGRAM HITUNG RATA-RATA          ')
print('------------------------------------------')
jumlah = 0
data = 0
lanjut = 'y'
while lanjut == 'y':
    try:
        bilbul = int(input('Masukkan bilangan bulat: '))
    except ValueError:
        print('Bukan bilangan bulat')
        bilbul = int(input('Masukkan bilangan bulat: '))
    jumlah += bilbul
    data += 1
    lanjut = input('Lagi (y/n)? :')
    if lanjut == 'n':
        rata = jumlah/data
        break
print('Rata-ratanya adalah ', rata)
