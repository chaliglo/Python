from Golfer import Golfer

class GolfCourse():

    sLocation = ""
    nHoleCount = 0
    nCoursePar = 0
    lListofHoles = []

    def __init__(self, location, par, numberOfHoles):
        self.sLocation = location
        self.nHoleCount = numberOfHoles
        self.nCoursePar = par
        self.lListofHoles = []

    def __str__(self):
        return self.sLocation + ", " + self.nCoursePar + ", " + self.nHoleCount + "\n" +"\n".join(map(str, self.lListofHoles))
