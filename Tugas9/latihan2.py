import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)
data = ''

lagi = 'y'
while lagi == 'y':
    file = open(path + '/latihan2.txt','a')
    nim = input('Masukkan NIM          : ')
    nama = input('Masukkan Nama Mahassiswa     : ')
    alamat = input('Masukkan Alamat       : ')
    dataAwal = [nim, nama, alamat]
    data = '|'.join(dataAwal) + '\n'
    file.write(data)
    lagi = input('Masukan input (y/n): ')
file.close()
file = open(path + '/latihan2.txt','a')
hasil = file.read( )
print(hasil)
file.close()
