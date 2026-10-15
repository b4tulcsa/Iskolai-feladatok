
#orai feladat
"""
lista = input("Adjon meg egy szóközzel elválasztott szósorozatot: ")
szo = lista.split(" ")
szam = len(szo)
elso = szo[0]
utolso = szo[-1]

print("A megadott szavak száma: ",szam)
print("Az első szó: ",elso)
print("Az utolsó szó: ",utolso)
"""
#orai feladat
lista = "55 44 1 20 50"#input("Adjon meg egy szóközzel elválasztott szósorozatot: ")
szo_szam = lista.split(" ")
szam =[]
for i in szo_szam:
    szam.append(int(i))

novekvo = szam.sort()
osszeg = sum(szam)
atlag = osszeg / len(szam)
minimum = min(szam)
maximum = max(szam)


print(f"A megadott számok összege: {osszeg}")
print(f"A megadott számok átlaga: {atlag}")
print(f"A megadott legkisebb szám: {minimum}")
print(f"A megadott legnagyobb szám: {maximum}")

"""A megadott számok összege: 170
A megadott számok átlaga: 34.0
A megadott legkisebb szám: 1
A megadott legnagyobb szám: 55"""