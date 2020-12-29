mahasiswa = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
            'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
            'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('=' * 70)
print('NIM'.ljust(12, ' '), end='')
print('NAMA'.ljust(25, ' '), end='')
print('TGL LAHIR'.ljust(15, ' '), end='')
print('TEMPAT LAHIR'.ljust(15))
print('-' * 70)

for data in range(len(mahasiswa)):
    data = mahasiswa[data]
    nim, nama, tgl, tempat = data.split(':')
    y, m, d = tgl.split('-')
    tanggal = ('/'.join([d, m, y]))
    print(nim.ljust(12, ' '), end='')
    print(nama.ljust(25, ' '), end='')
    print(tanggal.ljust(15, ' '), end='')
    print(tempat.ljust(15, ' '))
    
print('-' * 70)
