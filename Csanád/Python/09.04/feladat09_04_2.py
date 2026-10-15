class Game:
    def __init__(self,cim,mufaj,kiado,eladott,ev,koltseg,bevetel,jatekos):
        self.cim = cim
        self.mufaj = mufaj
        self.ertekeles = ertekeles
        self.kiado = kiado
        self.eladott = eladott
        self.ev = ev
        self.koltseg = koltseg
        self.bevetel = bevetel
        self.jatekos = jatekos

lista = []
cimek = []
jatekok = 0
fps_jatekok = []
legjobb_ertek = 0
legjobb_ertek_nev = ""
ertekeles = 0


with open("games_hun.csv","r",encoding="utf-8")as file:
    next(file)
    for line in file:
        l = line.strip().split(",")
        sor = Game(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
        cimek.append(sor.cim)
        jatekok += 1
        if l[1] == "FPS":
            fps_jatekok.append(sor.cim)
        if int(sor.ertekeles) > legjobb_ertek:
            legjobb_ertek = int(sor.ertekeles)
            legjobb_ertek_nev = sor.cim
        ertekeles += int(sor.ertekeles)  


print(cimek)
print(f"{jatekok}db játék van")
print(f" fps játékok: {fps_jatekok}")
print(legjobb_ertek_nev)
print(ertekeles/len(cimek))


