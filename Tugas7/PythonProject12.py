buah = {'apel' : 5000, 
    'jeruk' : 8500, 
    'mangga' : 7800, 
    'duku' : 6500}

while True:
    listA= ["Menu:",
    "A. Tambah data buah",
    "B. Beli buah",
    "C. Tampilkan data buah",
    "D. Hapus data buah ",
    "E. Tutup program"]

    for c in listA:
        print(c)
    print("Data buah: ", buah)
    menu = str(input("Pilihan anda (A/B/C/D/E) = "))

    
    if menu == "A" :
        nama = input("Masukkan nama buah    : ")
        harga = int(input("Masukkan harga satuan : "))
        ada = nama in buah.keys()
        if ada == True:
            print("Nama buah sudah ada")
        else:
            buah[nama] = harga
        print("Data buah: ")
        for x, y in buah.items() :
            print("-", x, "(Harga Rp", y, ")")
            
    elif menu == "B":
            jenis = list(buah) 
            harga = list(buah.values())
            tambah = 'y'
            total = 0
            while True:
                namaBuah = input("Nama buah yang dibeli: ") 
                berapakgyangdibeli = int(input("Berapa kg                        : ")) 
                indeks = jenis.index(namaBuah) 
                totalSementara = harga[indeks] * berapakgyangdibeli 
                total = total + totalSementara 
                tambah = input("Ingin beli buah yang lain(y/n)? ")
                if tambah == "n":
                    break
            print("____________________________________")

            print("Total harga                     : ", total)
          

    elif menu == "C": 
        for a,b in buah.items():
            print("harga ",a ," = ", b)

    elif menu == "D":
            hapus = str(input("nama buah yang ingin dihapus = "))
            del buah[hapus]
            print("Daftar buah= ", buah)
            break
        
    elif menu == "E":
            print("Thankyou")
            break
