def ubahHuruf(teks, a, b):
    listhuruf= list(teks)
    baru = []
    for g in range (len(listhuruf)):
        huruf = listhuruf[g]
        if huruf == a:
            huruf = b
        baru = baru + [huruf]
    hasil= "".join(baru)
    return hasil
y = ubahHuruf('MATEMATIKA', 'T', 'S')
print(y)
