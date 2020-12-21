def terbaik(data):
    rekap = [] 
    for a in range(len(data)):
        list = nilaiMhs[a] 
        nilaiAkhir = (list['mid'] + 2*list['uas']) / 3 
        rekap.append(nilaiAkhir) 
    terbaik = rekap.index(max(rekap)) 
    where = data[terbaik] 
    who = where['nama'] + " " + where['nim']
    return who

nilaiMhs = [{'nim' : 'A01', 'nama' : 'Oryza', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Pamungkas', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Elisabeth', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Jasmine', 'mid' : 50, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Laura', 'mid' : 70, 'uas' : 90}]

print("Nilai tertinggi draih oleh mahasiswa bernama ",terbaik(nilaiMhs))
