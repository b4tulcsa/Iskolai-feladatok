lista = "alma körte szilva barack"
lista1 = "körte barack meggy"
halmaz = lista.split(" ")
halmaz1 = lista1.split(" ")

for i in halmaz:
    halmaz1.append(i)

halmaz1 =set(halmaz1)
print(halmaz1)


