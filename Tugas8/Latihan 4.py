import random
def shuffleString(a,c):
    
    kata = list(a)
    listhasil = []
    listhasil1 = []
    while True:
        
        random.shuffle(kata) 
        hasil = "".join(kata)
        b = hasil in listhasil1
        
        if b == False:
            listhasil1 = listhasil1 + [hasil]

        if len(listhasil1)== c :
            listhasil = listhasil1
            break
    return listhasil

print(shuffleString('aku',2))
print(shuffleString('aku',3))
print(shuffleString('aku',4))
