bahasaindonesia = int(input("Nilai bahasa indonesia? "))
matematika = int(input("Nilai matematika? "))
ipa = int(input("Nilai ipa? "))


if (bahasaindonesia < 60) or (matematika < 70) or (ipa < 60):
    print("STATUS KELULUSAN : TIDAK LULUS")
elif (bahasaindonesia > 60) and(matematika > 70) and (ipa > 60):
    print("STATUS KELULUSAN : LULUS")

