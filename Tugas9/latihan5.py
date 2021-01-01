def hasil():
    data = open(file, "r")
    for x in data:
        x = x.split('|')
        jumlah = int(x[0]) + int(x[1])
        print(jumlah)
    data.close()

file = "latihan5.txt"
hasil()
