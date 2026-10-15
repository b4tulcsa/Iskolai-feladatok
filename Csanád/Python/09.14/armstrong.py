#Armstrong-szám
szamjegy = []

def armstrong_szam(n):
    osszeg = 0
    for szam in str(n):
        szamjegy.append(szam)
    
    for i in szamjegy:
        szm = int(i) ** len(szamjegy)
        osszeg += int(szm)

    if osszeg == n:
        return True
    else:
        return False

print(armstrong_szam(int(input("kérek egy számot: "))))