ossz_jatek = []
valaszok = []

class Jatekok:
    def __init__(self,cim:str,mufaj:str,kiado:str,ertekeles:int,eladott:float,megjelenes:int,koltseg:float,bevetel:float,jatekosok:float):
        
        self.cim = cim
        self.mufaj = mufaj
        self.kiado = kiado
        self.ertekeles = int(ertekeles)
        self.eladott = float(eladott)
        self.megjelenes = int(megjelenes)
        self.koltseg = float(koltseg)
        self.bevetel = float(bevetel)
        self.jatekosok = float(jatekosok)

file = open("Python/09.21/games-hun.csv", "r", encoding="utf-8")
next(file)

for sor in file:
    darabolt = sor.strip().split(",")
    jatek = Jatekok(darabolt[0],darabolt[1],darabolt[2],darabolt[3],darabolt[4],darabolt[5],darabolt[6],darabolt[7],darabolt[8])
    ossz_jatek.append(jatek)

#1
for jatek in ossz_jatek:
    valaszok.append(jatek.cim)

#2
valaszok.append(len(ossz_jatek))

#3
fps = 0
for jatek in ossz_jatek:
    if "FPS" in jatek.mufaj:
        fps += 1
valaszok.append(fps)

#4 
legnagyobb_ertekeles = 0
legnagyobb_ertekeles_jatek = ""
for jatek in ossz_jatek:
    if jatek.ertekeles > legnagyobb_ertekeles:
        legnagyobb_ertekeles = jatek.ertekeles
        legnagyobb_ertekeles_jatek = jatek.cim
        
valaszok.append(legnagyobb_ertekeles_jatek)

#5
ossz_ertekeles = 0
for jatek in ossz_jatek:
    ossz_ertekeles += jatek.ertekeles

valaszok.append(ossz_ertekeles/len(ossz_jatek))
#6
megjelenestizelott = []
for jatek in ossz_jatek:
    if jatek.megjelenes > 2010:
        megjelenestizelott.append(jatek.cim)

valaszok.append(megjelenestizelott)

#7
legtobb_eladas = 0
legtobb_eladas_nev = ""

for jatek in ossz_jatek:
    if jatek.eladott > legtobb_eladas:
        legtobb_eladas = jatek.eladott
        legtobb_eladas_nev = jatek.cim

valaszok.append(legtobb_eladas_nev)

#8
ossz_bevetel = 0
for jatek in ossz_jatek:
    ossz_bevetel += jatek.bevetel

valaszok.append(ossz_bevetel)

#9
valv = 0
for jatek in ossz_jatek:
    if jatek.kiado == "Valve":
        valv += 1

valaszok.append(valv)

#10
rpgk = []
for jatek in ossz_jatek:
    if "RPG" in jatek.mufaj:
        rpgk.append(jatek.cim)
valaszok.append(rpgk)

#11
fejl_kolt = 0
fejl_kolt_nev = ""
for jatek in ossz_jatek:
    if jatek.koltseg > fejl_kolt:
        fejl_kolt = jatek.koltseg
        fejl_kolt_nev = jatek.cim

valaszok.append(fejl_kolt_nev)

#12
fpsek = []
for jatek in ossz_jatek:
    if "FPS" in jatek.mufaj:
        fpsek.append(jatek.bevetel)
    
valaszok.append(sum(fpsek)/len(fpsek))

#13
ertekeleskilenvenot = []
for jatek in ossz_jatek:
    if jatek.ertekeles >= 95:
        ertekeleskilenvenot.append(jatek.cim)

valaszok.append(ertekeleskilenvenot)

#14
legtobb_jatekosok = 0
legtobb_jatekosok_nev = ""
for jatek in ossz_jatek:
    if jatek.jatekosok > legtobb_jatekosok:
        legtobb_jatekosok = jatek.jatekosok
        legtobb_jatekosok_nev = jatek.cim

valaszok.append(legtobb_jatekosok_nev)

#15
mufajok = []
for jatek in ossz_jatek:
    if jatek.mufaj not in mufajok:
        mufajok.append(jatek.mufaj)

valaszok.append(len(mufajok))

#16
megjelenestizutan = []
for jatek in ossz_jatek:
    if jatek.megjelenes < 2010:
        megjelenestizutan.append(jatek.cim +" "+ str(jatek.megjelenes))
valaszok.append(megjelenestizutan)
#17
ossz_kolt = 0
for jatek in ossz_jatek:
    ossz_kolt += jatek.koltseg

valaszok.append(str(ossz_kolt/len(ossz_jatek))+" millio")

#18
kiadok = dict()
for jatek in ossz_jatek:
    if jatek.kiado in kiadok:
        kiadok[jatek.kiado] += 1
    else:
        kiadok[jatek.kiado] = 1

kiadok_max = 0
kiadok_max_nev = ""
for i in kiadok:
    if kiadok[i] > kiadok_max:
        kiadok_max = kiadok[i]
        kiadok_max_nev = i

valaszok.append(kiadok_max_nev)

#19
ezerdollar = []
for jatek in ossz_jatek:
    if jatek.bevetel > 1000:
        ezerdollar.append(jatek.cim)

valaszok.append(ezerdollar)
#20
jaekosok = 0
for jatek in ossz_jatek:
    jaekosok += jatek.jatekosok

valaszok.append(str(jaekosok/len(ossz_jatek))+" millio")

print(valaszok)
