#Jármű:
#    lóerő: int
#    fogyasztás: float
#    szín: str

#Autó(Jármű):
#    ajtokszama: int


#Motor(Jármű):
#    bukosisak: bool

class Jarmu:
    def __init__(self, loero: int, fogyasztas: float, szin: str): # kontruktor
        self.loero = loero
        self.fogyasztas = fogyasztas
        self.szin = szin

    def hello(self):
        print("Hellóóóóó")



class Auto(Jarmu):
    def __init__(self, loero: int, fogyasztas: float, szin: str, ajtokszama: int):
        super().__init__(loero, fogyasztas, szin)

        # további extra tulajdonságok:
        self.ajtokszama = ajtokszama

    def szia(self):
        print("Szia")


class Motor(Jarmu):
    def __init__(self, loero: int, fogyasztas: float, szin: str, bukosisak: bool):
        super().__init__(loero, fogyasztas, szin)

        # további extra tulajdonságok:
        self.bukosisak = bukosisak 