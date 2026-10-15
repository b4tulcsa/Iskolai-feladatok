playlist = []

file = open("Python/09.17/playlist.csv", "r", encoding="UTF-8")

for i in file:
    sor = i.strip().split(";")
    playlist.append(sor)

def teljes_hossz():
    play_len = 0
    for i in playlist:
        play_len += int(i[3])
    
    file = open("Python/09.17/02_hossz.txt", "w", encoding="UTF-8")
    
    file.write(f"A lista hossza {play_len//60} perc, {play_len%60} mádodperc")
    
teljes_hossz()

def leghosszabb_rockzene():
    hossz = 0
    hossz_nev = ""
    for i in playlist:
        if i[2] == "rock":
            if int(i[3]) > int(hossz):
                hossz = int(i[3])
                hossz_nev = i[1]

    file = open("Python/09.17/03_leghosszabb_rock.txt", "w", encoding="UTF-8")
    
    file.write(hossz_nev)

leghosszabb_rockzene()

def leggyakoribb_mufaj():
    mufajok = dict()
    legtobbmufaj = "" 
    legtobbmufaj_num = 0

    for i in playlist:
        if i[2] in mufajok:
            mufajok[i[2]] += 1
        else:
            mufajok[i[2]] = 1
    
    for i in mufajok:
        if mufajok[i] > legtobbmufaj_num:
            legtobbmufaj_num = mufajok[i]
            legtobbmufaj = i

    file = open("Python/09.17/04_kedvenc_mufaj.txt", "w", encoding="UTF-8")
    
    file.write(legtobbmufaj)

leggyakoribb_mufaj()

def zeneket_csoportosit():
    eloadok = dict()
    for i in playlist:
        if i[0] in eloadok:
            eloadok[i[0]] += int(i[3])
        else:
            eloadok[i[0]] = int(i[3])

    file = open("Python/09.17/05_osszegzes.txt", "a", encoding="UTF-8")

    for i in eloadok:
        file.write(f"{i} - osszesen {eloadok[i]} masodpercnyi zene\n")

zeneket_csoportosit()