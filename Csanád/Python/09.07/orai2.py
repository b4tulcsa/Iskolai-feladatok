#Matematikai kondíciók igazságértéke
"""
if 5 < 3:
    print("Igaz")
else:
    print("Nem")

a = 0
b = 1

es = a and b
vagy = a or b
kizarovagy = a ^ b

print(a, b, es, vagy, kizarovagy)
"""

#1 
print("Fagypont mérése")
print("")
ho = float(input("Adj meg egy homersekletet: "))

if ho > 0:
    print("A hőmérséklet nincs fagypont alatt.")
elif ho < 0:
    print("A hőmérséklet fagypont alatti.")
else:
    print("A hőmérséklet pontosan fagyponton van.")

print("Számológép")
print("")

szm1 = float(input("Elso szam: "))
szm2 = float(input("Masodik szam: "))
muv = input("Muvelet: ")

if muv == "+":
    print(f"Az eredmeny: {szm1 + szm2}")
elif muv == "-":
    print(f"Az eredmeny: {szm1 - szm2}")
elif muv == "*":
    print(f"Az eredmeny: {szm1 * szm2}")
elif muv == "/" or muv == ":":
    if szm2 != 0:
        print(f"Az eredmeny: {szm1 / szm2}")
    else:
        print("Ejnye, nullaval nem osztunk!")
else:
    print("Hibas muveleti jel!")

print("Gyakorlati jegy")
print("")

pont = int(input("A pontszamod: "))

if pont >= 85 and pont <= 100: #5 os
    print("Az erdemjegyed: Jeles (5)")
elif pont >= 70 and pont <= 84: #4 es
    print("Az erdemjegyed: Jó (4)")
elif pont >= 55 and pont <= 69: #3 as
    print("Az erdemjegyed: Közepes (3)")
elif pont >= 40 and pont <= 54: #2 es
    print("Az erdemjegyed: Elégséges (2)")
elif pont >= 0 and pont <= 39: #1 es
    print("Az erdemjegyed: Elégtelen (1)")
else:
    print("Ervenytelen ertek!")

print("Haromszog egyenlotlenseg")
print("")

a = int(input("Add meg az első oldal hosszát: "))
b = int(input("Add meg a masodik oldal hosszát: "))
c = int(input("Add meg a harmadik oldal hosszát: "))

if a < b + c and b < a + c and c < a + b:
    print("A megadott szakaszok alkothatnak háromszöget.")
else:
    print("A megadott szakaszok nem alkothatnak háromszöget.")