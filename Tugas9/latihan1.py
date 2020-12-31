myfile = open ('d:\latihan1.txt',)
angka = myfile.readlines()

gnp = []
gnjl = []

for b in range ( len ( angka )):
    nmbr = angka [b]
    if int(nmbr) % 2  == 0 :
        gnp = gnp + [nmbr]
    else :
        gnjl = gnjl + [nmbr]

print('Banyaknya bilangan genap : ', len(gnp))
print('Banyaknya bilangan ganjil: ', len(gnjl))
