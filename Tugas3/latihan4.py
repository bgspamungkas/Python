import math

jarakkotaAB= 125
kecepatankotaAB= 62
jarakkotaBC= 256
kecepatankotaBC= 70

waktukotaAB= (math.ceil (jarakkotaAB/kecepatankotaAB*60))
waktukotaBC= (math.ceil (jarakkotaBC/kecepatankotaBC*60))
istirahat= 45

jumlahwaktu= (waktukotaAB+waktukotaBC+istirahat)

waktuawal= 6
jumlahwaktudalamjam= (jumlahwaktu//60)+waktuawal
jumlahwaktudalammenit= (jumlahwaktu%60)

print('Pak Amir sampai dikota C pukul', (jumlahwaktudalamjam),'.',(jumlahwaktudalammenit) )
