def buahtermahal(buah):
    jenis = list (buah.keys())
    harga = list (buah.values()) 
    maks = max (harga) 
    b = harga.index (maks) 
    termahal = jenis [b]
    print("Harga buah termahal = ", termahal)
    
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500 }

buahtermahal(buah)
