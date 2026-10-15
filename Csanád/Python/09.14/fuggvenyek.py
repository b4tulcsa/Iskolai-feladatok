

#1
szoveg = input("Írj be egy szöveget: ")
kis = szoveg.lower()
print(kis)

#2
szoveg = input("Írj be egy szöveget: ")
szoveg_valt = szoveg.replace("e", "x")
print(szoveg_valt)

#3
szoveg = input("Írj be egy szöveget: ")
lista = szoveg.split(",")
print(lista)

#4
szm1 = int(input("Írj be egy számot: "))
szm2 = int(input("Írj be még egy számot: "))

legnagyobb = max(szm1, szm2)

print(legnagyobb)

#5
szoveg = input("Írj be számokat szóközzel elválasztva: ")
szoveg_split = szoveg.split(" ")
szamok = []

for szam in szoveg_split:
    szamok.append(int(szam))

atlag = sum(szamok) / len(szamok)
kerek = round(atlag, 3)

print(f"Az átlag: {kerek}")

#6 valami faktoriális
import math 
szm = int(input("Írj be egy számot: "))
print(f"{szm}! = {math.factorial(szm)}")

#7 
import math 
rad = int(input("Írj be egy szöget radiánban: "))
fok = math.degrees(rad)

print(f"{rad} rad = {fok} fok")

#8
import datetime

ido = datetime.datetime.now()
nap = ido.strftime("%j")
print(nap)

#9
import datetime
ido = input("Írj be egy dátumot (yyyy-mm-dd): ")
ido_valaszt = ido.split("-")

ev = int(ido_valaszt[0])
ho = int(ido_valaszt[1])
nap = int(ido_valaszt[2])

datum = datetime.datetime(ev, ho, nap)
szam = datum.strftime("%j")
hetnap = datum.strftime('%A')

print(f"Ma az év {szam}. napja van, ami {hetnap}.")

#10
import random
print(random.randint(1,100))

#11
import random
lista = []
for i in range(1,4):
    szo = input(f"Írj be egy szót ({i}.): ")
    lista.append(szo)

print(f"Kiválasztott szavak: {random.sample(lista, 2)}")

#12
def terulet_szamitas(hossz, szel):
    return hossz * szel

print(terulet_szamitas(5,10))

#13
def koszonto_uzenet(nev="Tanuló"):
    print(f"Üdvözöllek {nev}!")

koszonto_uzenet()
koszonto_uzenet("Katalin")

#14
import math
def kor_kerulete(r):
    return 2 * math.pi * r

print("Kör kerülete:", kor_kerulete(7))

#15
def osszead(a=0, b=0):
    return a + b

print(osszead(5, 1)) #1+5
print(osszead(5)) #5+0
print(osszead()) #0+0
