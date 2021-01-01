buka = open("d:\latihan2.txt", "r")
file = buka.readlines()
fileMahasiswa = {}

for b in range(len(file)):

    mahasiswa = file[b]   
    nim, nama, alamat = mahasiswa.split('|')
    alamat = alamat.replace('\n', '')   
    fileMhs = {'nim': nim, 'nama': nama, 'alamat': alamat}
    fileMahasiswa[nama] = fileMhs

print(fileMahasiswa)
buka.close()
