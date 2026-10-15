#tanulok atlaga
osztaly = []
atlag = 0
for i in range(5):
    diak = int(input(f"Add meg az {i+1}. tanuló jegyét: "))
    osztaly.append(diak)
for f in osztaly:
    atlag += f

novekvo = sorted(osztaly)
csokkeno = sorted(osztaly, reverse=True)
print(f"Az osztály átlaga: {atlag/len(osztaly)}")
#sorrendek
print(f"Tanulók jegyei növekvő sorrendben: {novekvo}")
print(f"Tanulók jegyei csökkenő sorrendben: {csokkeno}")

#Legjobb és legrosszabb jegy
print(f"Legjobb jegy: {csokkeno[0]}")
print(f"Legkissebb jegy: {novekvo[0]}")

#honapok
honapok = ["Január","Február","Március","Április","Május","Június","Július","Augusztus","Szeptember","Október","November","December"]
pay = []
ossz = 0
for i in range(12):
    kolt = int(input(f"A(z) {honapok[i]} havi költsége: "))
    pay.append(kolt)

novekvo = sorted(pay)
csokkeno = sorted(pay, reverse=True)
for z in pay:
    ossz += z

print(f"Az éves rezsi költség: {sum(pay)}")
print(f"Átlagos havi rezsi költség: {sum(pay)/len(pay)}")
print(f"A maximum havi rezsi költség: {csokkeno[0]}")
print(f"A minimum havi rezsi költség: {novekvo[0]}")


#kiárúsítás
darab = int(input("Add meg a termékek darabszámát: "))
arak = []
learazott = []
for i in range(darab):
    item = int(input(f"Add meg az {i+1}. termék árát: "))
    arak.append(item)

print("Eredeti árak: ",arak)

for i in arak:
    learazott.append(round(i*0.7))

print("Az akciós árak: ",learazott)
print("Az akciós átlagár: ",round(sum(learazott)/len(learazott)))

#kolcsonozesi rendszer
konyvek = {}
konyvidok = []

for i in range(5):
    kony = input(f"Add meg a {i+1}. könyv címét: ")
    konyvek[kony] = ido
    ido = int(input("Könyv kölcsönzési ideje: "))
    konyvidok.append(ido)

print("Leghosszabb kölcsönzési idő: ",min(konyvidok))
print("Legrövidebb kölcsönzési idő: ",max(konyvidok))

#Szövegelemzés
