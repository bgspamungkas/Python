bahasaindonesia = int(input("Nilai bahasa indonesia? "))
matematika = int(input("Nilai matematika? "))
ipa = int(input("Nilai ipa? "))

if (bahasaindonesia <=0  and bahasaindonesia <=100):
    print("Maaf input ada yang tidak valid")
elif (matematika <=0  and matematika <=100):
    print("Maaf input ada yang tidak valid")
elif (ipa <=0  and ipa <=100):
    print("Maaf input ada yang tidak valid")
    
elif(bahasaindonesia < 60 or matematika < 70 or ipa < 60):
    print("STATUS KELULUSAN : TIDAK LULUS")
    print("SEBAB : ")
    if(bahasaindonesia < 60): 
        print("Nilai bahasa indonesia kurang dari 60")
    if (matematika < 70):
        print("Nilai matematika kurang dari 70")
    if (ipa < 60):
        print("Nilai ipa kurang dari 60")
        
elif(bahasaindonesia > 60 or matematika > 70 or ipa > 60):
    print("STATUS KELULUSAN : LULUS")
    
