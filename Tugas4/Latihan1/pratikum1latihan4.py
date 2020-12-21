#Coding struk gaji 

KodeKaryawan = int(input('Masukkan kode karyawan : '))
NamaKaryawan = input('Masukkan nama karyawan : ')
Golongan = input('Masukan golongan : ')

print('===========================================================')
print('STRUK GAJI KARYAWAN')
print('-----------------------------------------------------------')
print('Nama Karyawan :' + NamaKaryawan + '(Kode Karyawan :' +
str(KodeKaryawan) + ')')
print('Golongan :' + Golongan)
print('-----------------------------------------------------------')

if(Golongan == 'A'):
     GajiPokok = 10000000
     Potongan = 2.5
     Jumlahpotongan = 2.5 / 100 * 10000000
     GajiBersih = 10000000 - Jumlahpotongan
 
elif(Golongan == 'B'):
     GajiPokok = 8500000
     Potongan = 2.0
     Jumlahpotongan = 2.0 / 100 * 8500000
     GajiBersih = 8500000 - Jumlahpotongan
 
elif(Golongan == 'C'):
     GajiPokok = 7000000
     Potongan = 1.5
     Jumlahpotongan = 1.5 / 100 * 7000000
     GajiBersih = 7000000 - Jumlahpotongan
 
elif(Golongan == 'D'):
     GajiPokok = 5500000
     Potongan = 1.0
     Jumlahpotongan = 1.0 / 100 * 5500000
     GajiBersih = 5500000 - Jumlahpotongan

print('GajiPokok : Rp' + str(GajiPokok))
print('Potongan (' + str(Potongan) + '%): Rp' + str(Jumlahpotongan))
print('-----------------------------------------------------------')
print('GajiBersih : Rp' + str(GajiBersih))

