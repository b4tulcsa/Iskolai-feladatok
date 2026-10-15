#1
eredeti_ar = int(input("Az alkatresz jelenlegi ara: "))
emel = float(input("Aremeles (szazalekban): "))

valtozott_ar = eredeti_ar + (eredeti_ar * (emel/100))

print(valtozott_ar)

#2
suly = float(input("Add meg a súlyodat (KG): "))
valasztas = int(input("Milyen az aktivitási szinted? (1 - átlagos, 2 - magas, 3 - extrém): "))
if valasztas == 1:
    feherje = suly * 0.8
    print(f"A napi fehérje szükségleted: {feherje} gramm")
elif valasztas == 2:
    feherje = suly * 1.2
    print(f"A napi fehérje szükségleted: {feherje} gramm")
elif valasztas == 3:
    feherje = suly * 2
    print(f"A napi fehérje szükségleted: {feherje} gramm")
else:
    print("Hibás aktivitási szint!")

#3
tav = int(input("Kérem a megtett távolságot (km): "))
felhasznalt = float(input("Kérem a felhasznált üzemanyag mennyiségét (liter): "))
fogyasztas = felhasznalt/tav*100

print(f"Az átlagos üzemanyag fogyasztás: {round(fogyasztas, 2)} liter/100km")

#4

for i in range(100):
    print("Laci")
