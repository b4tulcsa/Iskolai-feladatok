#Elmozdulás
def elmozdulas(szoveg:str):
    vert = 0
    hor = 0

    for betu in szoveg:
        if betu == "F":
            vert += 1
        elif betu == "L":
            vert += -1
        elif betu == "J":
            hor += 1
        elif betu == "B":
            hor += -1
        
        if hor < 0:
            helmozd = "balra"
        else:
            helmozd = "jobbra"

        if vert < 0:
            velmozd = "le"
        else:
            velmozd = "fel"

    return f"{abs(hor)} lepes {helmozd}, {abs(vert)} lepes {velmozd}"
    
print(elmozdulas("FBLLLJLLJ"))