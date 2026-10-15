#1
'''
def abszolut(a, b):
    a = abs(a)
    b = abs(b)
    if a>b:
        return a
    if a == b:
        return a,b
    else:
        return b

print(abszolut(int(input("kérek egy számot: ")), int(input("kérek egy számot: "))))
'''
#2

def jelszo_erosseg(j):

    erosseg = 1

    if len(j) >= 8:
        erosseg += 2

    if len(j) >= 8:
        erosseg += 1

    for i in j:
        eros = ["-","_","."]
        if i in eros:
            erosseg += 2

    if len(j) == 0:
        erosseg = 0

    if "123" in j or "jelszo" in j:
        erosseg = 0

    return erosseg

jelszo = input("kérek egy jelszót: ")
print(jelszo_erosseg(jelszo))

