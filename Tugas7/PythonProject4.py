sayuran = ["bayam", "kangkung", "wortel", "selada"]
while True:
    listA= ["Menu:",
    "A. Tambah data sayuran",
    "B. Hapus data sayuran",
    "C. Tampilkan data sayuran",
    "D. Berhenti",
    "Daftar Sayuran (bayam, kangkung, wortel, selada)"]

    for b in listA:
        print(b)

    
    menu = str(input("pilihan anda (A/B/C/D) = "))

    if menu == "A":
        tambahan = str(input("nama sayuran yang  ditambahakan = "))
        if tambahan in sayuran:
            print("Sayuran sudah ada")
        else:
            sayuran.append(tambahan)
            print("perubahan data sayuran = ", sayuran)
        
    elif menu == "B":
        try:
            hapus = str(input("nama sayuran yang  dihapus = "))
            sayuran.remove(hapus)
            print("Daftar sayuran = ", sayuran)
        except ValueError:
            print("data tidak ditemukan")

    elif menu == "C":
        print("Daftar sayuran = ", sayuran)

    elif menu=="D":
        print("Thankyou")
        break
    else:
        print("tidak ditemukan")
