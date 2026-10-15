class Suti:
    def __init__(self,nev,tipus,ar):
        self.nev = nev
        self.tipus = tipus
        self.ar = int(ar)
                      
osszsuti = []
vegyesar = 0

file = open("Python/09.25/cuki.txt","r",encoding="utf-8")
for sor in file:
    sort = sor.strip().split(";")
    desszert = Suti(sort[0],sort[1],sort[2])
    osszsuti.append(desszert)

file.close()

for suti in osszsuti:
    if suti.tipus == "vegyes":
        vegyesar += suti.ar



        
print(f'A cuki.txt-ben összesen {len(osszsuti)} sütemény található.')
print(f"  A vegyes sütemények ára összesen {vegyesar} Ft.")

tipusok = dict()

for suti in osszsuti:
    if suti.tipus not in tipusok:
        tipusok[suti.tipus] = 1
    else:
        tipusok[suti.tipus] += 1

for i in tipusok:
    print(f"{i}: {tipusok[i]}")

file = open("Python/09.25/akciosTortak.txt","w",encoding="utf-8")
iras = ""

for suti in osszsuti:
    if suti.tipus == "torta" and suti.ar < 10000:
        iras += (f"{suti.nev} új ára {round(suti.ar - suti.ar * 0.1)}\n")

file.write(iras)

file.close()