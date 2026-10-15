#Szövegtömörítés
def tomorit(szoveg:str):
    betuszam = 1
    elozobetu = " "
    ujszoveg = ""

    for betu in szoveg:
        if elozobetu != betu:
            print(f"a betuszam: {betuszam} az elozo betu: {elozobetu} a betu: {betu}")
            elozobetu = betu
            if betuszam >= 2:
                print(elozobetu)
                ujszoveg += str(betuszam)+betu
                betuszam = 1
            else:
                ujszoveg += betu
        else:
            betuszam+=1


    return ujszoveg
print(tomorit("Hahooooo! Van itt valaki???"))

