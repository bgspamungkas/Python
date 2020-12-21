buah = ["kiwi", "semangka", "blimbing", "wortel"]
print("Data buah = ", buah)

def sortStringByChar(buah):
    buah.sort(key = len, reverse = True)
    print("Data buah berdasarkan banyak karakter = ", buah)
    
sortStringByChar(buah)
