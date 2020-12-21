print("Daftar harga buah per kilogram: ")
daftar = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

y = 0
for a,b in daftar.items():
    y += 1
    print(y ,".", a ,"=",b)

jenis = list(daftar) 
harga = list(daftar.values())
namaBuah = input("Nama buah yang dibeli: ") 
berapakgyangdibeli = int(input("Berapa kg            : "))

print("-------------------------------------------")

indeks = jenis.index(namaBuah) 
total = harga[indeks] * berapakgyangdibeli 
print("Total harga          : ", total)
