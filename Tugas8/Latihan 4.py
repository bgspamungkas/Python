import random
def shuffleString(x,n):
    kata = list(x)
    listhasil = []
    listhasil1 = []
    while True:
        random.shuffle(kata) 
        hasil = "".join(kata)
        b = hasil in listhasil1
        if b == False:
            listhasil1 = listhasil1 + [hasil]
        if len(listhasil1)== n :
            listhasil = listhasil1
            break
    return listhasil
print(shuffleString('aku',2))
print(shuffleString('aku',3))
print(shuffleString('aku',4))
