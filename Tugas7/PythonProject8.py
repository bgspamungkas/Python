buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
harga = list(buah.values()) 

rataRata= sum(harga) / len(harga)
print("Rata-rata harga buah = ",rataRata)
