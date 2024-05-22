class Hole():
    nName = ""
    nHoleNumber = 0
    nPar = 0

    def __init__(self, hole, name, par):
        self.nHoleNumber = hole
        self.nPar = par
        self.nName = name

    def __str__(self):
        return "Hole" + self.nHoleNumber + " - " + "par " + self.nPar