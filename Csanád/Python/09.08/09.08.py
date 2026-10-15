
#paros szamok osszege
osszeg = 0
sz1 = int(input("Az intervallum also vegpontja: "))
sz2 = int(input("Az intervallum felso vegpontja: "))
for i in range(sz1,sz2+1,2):
    osszeg += i
else:
    print(f"A(z) [{sz1}; {sz2}] intervallumba eso paros szamok osszege: {osszeg}")

#prima nyeremenyjatek

csoki = int(input("Add meg a csoki gyartasi sorszamat: "))
osztok = 0
if csoki >= 1:
    for i in range(1,csoki+1):
        if csoki % i == 0:
            osztok += 1

if osztok == 2:
    print("Gratulalok, nyertel!")
else:
    print("Sajnos nem nyert!")
    
#szorzotábla

for x in range(1,11):
    for y in range(1,11):
        print(x*y,end=" ")
    print("")

#fibonacchi
"""
n=int(input)
elso = 0
masodik = 1
fibonacchi = []

def fibo(n):
    for i in range(n):
        fibonacchi.append(elso + masodik)
        elso + masodik = masodik
        masodik = elso
"""

