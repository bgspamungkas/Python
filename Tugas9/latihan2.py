import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)
data = ''

lagi = 'y'
while lagi == 'y':
    myfile = open(path + '/latihan2.txt','a')
    nim = input('Masukkan NIM          : ')
    nama = input('Masukkan Nama Mahassiswa     : ')
    alamat = input('Masukkan Alamat       : ')
    dataAwal = [nim, nama, alamat]
    data = '|'.join(dataAwal) + '\n'
    myfile.write(data)
    lagi = input('Masukan input (y/n): ')
    
myfile.close()
myfile = open(path + '/latihan2.txt','r')
hasil = myfile.readlines()
print(hasil)
myfile.close()
