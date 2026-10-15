"""class Music:
    def __init__(self,cim,mufaj,hossz,zenesz):
        self.cim = cim
        self.mufaj = mufaj
        self.hossz = hossz
        self.zenesz = zenesz"""

ido = 0
leghosszabb_nam = ""
lehhosszabb_hossu = 0

with open("music.csv","r",encoding="utf-8")as file:
    for line in file:
        l = line.strip().split(";")
        ido += int(l[-1])
        if l[2] == "rock":
            if int(l[-1]) > lehhosszabb_hossu:
                lehhosszabb_hossu = int(l[-1])
                leghosszabb_nam = l[1]



with open("02_hossz.txt","w",encoding="utf-8") as f:
    f.write(f"a playlist {int(ido/60)} perc és {ido%60} másodperc hosszú")
with open("03_leghosszabb_rock.txt","w",encoding="utf-8") as f:
    f.write(leghosszabb_nam)


