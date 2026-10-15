#Jeles (5)	85-100%
#Jó (4)	70-84%
#Közepes (3)	55-69%
#Elégséges (2)	40-54%
#Elégtelen (1)	0-39%

jegy = ""

pont = int(input("kérem az elért pontszámot: "))

while pont > 100 or pont < 0:
    pont = int(input("kérem az elért pontszámot: "))

if pont >= 0 and pont <= 39:
    jegy = "Elégtelen (1)"
elif pont >= 40 and pont <= 54:
    jegy = "Elégséges (2)"
elif pont >= 55 and pont <= 69:
    jegy = "Közepes (3)"
elif pont >= 70 and pont <= 84:
    jegy = "Jó (4)"
elif pont >= 85 and pont <= 100:
    jegy = "Jeles (5)"

print(f"   A megadott százalékhoz tartozó érdemjegy: {jegy}")