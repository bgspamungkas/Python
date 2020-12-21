namaFile = input("Masukkan nama file : ")

try:
    file = open (namaFile, "r") 
    print('Isi dari file', namaFile, 'adalah ')
    print(file.read()) 
except FileNotFoundError:
	print('Maaf file tidak ditemukan')
