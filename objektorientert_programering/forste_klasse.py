class Menneske:
    def __init__(self, navn, alder, yrke, hoyde):
        self.navn = navn 
        self.alder = alder
        self.yrke = yrke
        self.hoyde = hoyde

    def presenter(self):
        print("Hei jeg heter", self.navn)

    def bliEldre(self):
        print("Jeg var", self.alder , " år gammel")
        self.alder += 1 
        print("Nå er jeg", self.alder, " år gammel")

    def jobb(self):
        print("Mennesket jobber")

class Laerer(Menneske):
    def __init__(self, navn, alder, yrke, hoyde, elever):
        super().__init__(navn,alder,yrke,hoyde)

        self.elever = elever

    def retteProve(self):
        print(f"{self.navn} rettet en prøve")

    def jobb(self):
        print("Læreren jobber")

class Pilot(Menneske):
    def jobb(self):
        print("Piloten flyr")

class Elev(Menneske):
    def jobb(self):
        print("Eleven studerer")



ola = Laerer("Ola", 14, "Lærer", 187, 6)
kari = Pilot("Kari", 14, "Pilot", 134)
filip = Elev("Filip", 69, "Elev", 99)
maja = Elev("Maja", 67, "Elev", 177)

print(ola.alder)
print(kari.alder)
print(filip.alder)
print(maja.alder)

ola.presenter()
ola.bliEldre()
ola.retteProve()

ola.jobb()
kari.jobb()
filip.jobb()
maja.jobb()

arbeidere = [ola,kari,filip,maja]

for arbeider in arbeidere:
    arbeider.jobb()
