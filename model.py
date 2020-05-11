STEVILO_DOVOLJENIH_NAPAK = 10

# Konstante za rezultate ugibanj.
PRAVILA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"

# Konstante za zmago in poraz.
ZMAGA = "w"
PORAZ = "X"

bazen_besed = []
with open("Vislice\besede.txt") as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())

class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke
