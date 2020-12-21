KodeKaryawan = int(input('Masukkan kode karyawan : '))
NamaKaryawan = input('Masukkan nama karyawan : ')
Golongan = input('Masukan golongan : ')
status = input ('Masukan status((1: sudah menikah, 2: belum menikah) :')

if(status == '1'):
    totalanak = int(input("Masukan total anak : "))
    tunjanganmenikah = 10/100
    tunjangananak = 5/100 * totalanak
    status = "Sudah Menikah"

else:
    (status == '2')
    totalanak = 0
    tunjanganmenikah = 0
    tunjangananak = 0
    status ="Belum Menikah"
    

print('===========================================================')
print('STRUK GAJI KARYAWAN')
print('-----------------------------------------------------------')
print('Nama Karyawan :' + NamaKaryawan + '(Kode Karyawan :' +
str(KodeKaryawan) + ')')
print('Golongan :' + Golongan)
print('status :' + status)
print('totalanak :' + str(totalanak))
print('-----------------------------------------------------------')

if(Golongan == 'A'):
     GajiPokok = 10000000
     Potongan = 2.5
     Jumlahtunjanganmenikah = 10000000 * tunjanganmenikah
     Jumlahtunjangananak = 10000000 * tunjangananak
     Gajikotor = GajiPokok + Jumlahtunjanganmenikah + Jumlahtunjangananak
     Jumlahpotongan = 2.0/100 * Gajikotor
     GajiBersih = 10000000 - Jumlahpotongan
 
elif(Golongan == 'B'):
     GajiPokok = 8500000
     Potongan = 2.0
     Jumlahtunjanganmenikah = 8500000 * tunjanganmenikah
     Jumlahtunjangananak = 8500000 * tunjangananak
     Gajikotor = GajiPokok + Jumlahtunjanganmenikah + Jumlahtunjangananak
     Jumlahpotongan = 2.0 / 100 * Gajikotor
     GajiBersih = 8500000 - Jumlahpotongan
     
elif(Golongan == 'C'):
     GajiPokok = 7000000
     Potongan = 1.5
     Jumlahtunjanganmenikah = 7000000 * tunjanganmenikah
     Jumlahtunjangananak = 7000000 * tunjangananak
     Gajikotor = GajiPokok + Jumlahtunjanganmenikah + Jumlahtunjangananak
     Jumlahpotongan = 1.5 / 100 * Gajikotor
     GajiBersih = 7000000 - Jumlahpotongan
 
elif(Golongan == 'D'):
     GajiPokok = 5500000
     Potongan = 1.0
     Jumlahtunjanganmenikah = 5500000 * tunjanganmenikah
     Jumlahtunjangananak = 5500000 * tunjangananak
     Gajikotor = GajiPokok + Jumlahtunjanganmenikah + Jumlahtunjangananak
     Jumlahpotongan = 1.0 / 100 * Gajikotor
     GajiBersih = 5500000 - Jumlahpotongan

print('GajiPokok : Rp' + str(GajiPokok))
print('Tunjangan Istri/Suami : Rp' + str(Jumlahtunjanganmenikah))
print('Tunjangan Anak : Rp' + str(Jumlahtunjangananak))
print('-----------------------------------------------------------')
print('Gaji Kotor : Rp' + str (Gajikotor))
print('Potongan (' + str(Potongan) + '%): Rp' + str(Jumlahpotongan))
print('-----------------------------------------------------------')
print('GajiBersih : Rp' + str(GajiBersih))


