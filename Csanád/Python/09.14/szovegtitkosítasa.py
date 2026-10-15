#Szöveg titkosítása

def kodol(n,c,szoveg):
    kod = ""
    for i in szoveg:
        kod += i
        kod += n*c

    return kod

print(kodol(3,"x","Pizza delben?"))