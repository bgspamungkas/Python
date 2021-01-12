from datetime import *

def book(code, name, title):
    file = open(myfile, "a")
    time = datetime.date(datetime.now())
    timeBack = time + timedelta(days=7)
    data = [code, name, title, str(time), str(timeBack)]
    file.write('|'.join(data) + "\n")
    file.close

    
myfile = "datapeminjaman.txt"

while True:
    code = str(input("\nMasukan Kode Member\t: "))
    code = code.upper()
    name = str(input("Masukan Nama Member\t: "))
    title = str(input("Masukan Judul Buku\t: "))
    book(code, name, title)
    jawab = None
    while jawab not in ("y", "n"):
        jawab = str(input("\nUlangi lagi (y/n)\t: "))
        if jawab == "y":
            continue
        elif jawab == "n":
            exit()
        else:
            print("Masukan Pilihan (y/n)")
