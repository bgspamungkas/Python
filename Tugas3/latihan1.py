# program hitung tarif sewa mobil

jammulai = 6 
jamselesai = 23 
menitmulai = 0//60
menitselesai = 50//60

print ('Lama Sewa')
lamasewa =(jamselesai - jammulai)+ (menitselesai - menitmulai)
print(lamasewa)

waktu1= 12
waktu2= (lamasewa-waktu1)


tarif1 = 200000
tarif2 = (waktu2*10000)

print('Total biaya sewa')
total= (tarif1+tarif2)
print (total)
