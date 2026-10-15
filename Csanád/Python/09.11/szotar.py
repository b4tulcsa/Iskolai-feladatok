#ország fovaros
orszagok = {
    "Magyarország": "Budapest",
    "Németország": "Berlin"
}

kerdes = input("Melyik ország fővárosát szeretné megtudni? ")
if kerdes in orszagok:
    print("Magyarország fővárosa: ",orszagok.get(kerdes))
else:
    print("Az ország nem található a szótárban.")


#diak jegy
diak = {}

diak_behivott = input("Adja meg a diák nevét és jegyét: ")
lista = diak_behivott.split(" ")

diak[lista[0]] = lista[1]

print("jegyek ", diak)
