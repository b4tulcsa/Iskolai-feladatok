#karakter:
#    nev: str
#    rend: str
#    lezerkard: str
#    midiklorian:str

karakterek = list()

class Karakter:
    def __init__(self, nev: str, rend: str, lezerkard: str, midiklorian: int):
        self.nev = nev
        self.rend = rend
        self.lezerkard = lezerkard
        self.midiklorian = int(midiklorian)

    def __str__(self):
        return f"{self.nev} {self.rend} {self.lezerkard} {self.midiklorian}"
    
file = open("python/09.21/star-wars.csv","r",encoding="utf-8")
next(file)
for sor in file:
    darab = sor.strip().split(",")
    
    karakter = (Karakter(darab[0], darab[1], darab[2], darab[3]))
    karakterek.append(karakter)

midi = 0

for ember in karakterek:
    midi += ember.midiklorian

print(f"Az átlagos midiklorian szám: {midi/len(karakterek)}")

legkisebb = karakterek[0]

for p in karakterek:
    if p.midiklorian < legkisebb.midiklorian:
        legkisebb = p

print(f"A legkisebb midiklorian számú karakter: {legkisebb.nev} ({legkisebb.midiklorian})")

lezerkard_szinek = dict()

for p in karakterek:
    szin = p.lezerkard

    if szin in lezerkard_szinek:
        lezerkard_szinek[szin] += 1
    else:
        lezerkard_szinek[szin] = 1

print(lezerkard_szinek)

skywalker = 0

for p in karakterek:
    if "Skywalker" in p.nev:
        skywalker += 1

print(skywalker)


karakterek.sort(key=lambda x: x.midiklorian)

for p in karakterek:
    print(p) 