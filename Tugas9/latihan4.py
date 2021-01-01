myfile = open("latihan2.txt", "r")
file = myfile.readlines()
s = 0
baru = []

for lists in file :
    Mahasiswa = str(file [s])
    Mahasiswa = Mahasiswa.split('|')
    baru.append(Mahasiswa)
    s += 1

search = input('Masukkan NIM yang mau dicari : ')
hasil = False
b = 0
for x in baru:
    if search in baru[b]:
        g = 0
        for lists in baru:
            if search == baru[g][0]:
                print('Data Mahasiswa')
                print('NIM\t : '+ baru[g][0])
                print('Nama\t : '+ baru[g][1])
                print('Alamat\t : '+ baru[g][2])
                hasil = True
                break
            else:
                g += 1
    b += 1

if hasil == False :
    print('Data mahasiswa tidak ditemukan')
