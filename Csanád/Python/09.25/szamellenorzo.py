import math
szm = float(input("kérek egy számot: "))

if szm == 0:
    print("a szám nulla")
else:
    if szm > 0:
        print("a szám pozitív.")
    else:
        print("a szám negatív.") 

    if szm % 2 == 0:
        print("a szám páros.")
    else:
        print("a szám páratlan.")

    print(f"a szám gyökértéke: {math.sqrt(szm)}")