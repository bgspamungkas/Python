print("Daftar harga buah per kilogram: ")
daftar = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

y = 0
for a,b in daftar.items():
    y += 1
    print(y ,".", a ,"=",b)

jenis = list(daftar) 
harga = list(daftar.values())
tambah = 'y'
total = 0
while True:
    namaBuah = input("Nama buah yang dibeli: ") 
    berapakgyangdibeli = int(input("Berapa kg            : ")) 
    indeks = jenis.index(namaBuah) 
    totalSementara = harga[indeks] * berapakgyangdibeli 
    total = total + totalSementara 
    tambah = input("Ingin beli buah yang lain(y/n)? ")
    if tambah == "n":
        break
print("____________________________________")

print("Total harga          : ", total)
