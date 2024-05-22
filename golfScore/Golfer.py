from Hole import Hole

class Golfer():
    aName = ""
    lScore = []

    def __init__(self, golfer):
        self.aName = golfer
        self.lScore = []

    def __str__(self):
        return self.aName + "\n" + "\n".join(map(str, self.lScore)) + "\n"
    
    # Got help from ChatGPT
    def ScoreType(score, par):
        diff = score - par
        if diff == -2:
            return "Ace or Eagle"
        elif diff == -1:
            return "Birdie"
        elif diff == 0:
            return "Par"
        elif diff == 1:
            return "Bogey"
        elif diff == 2:
            return "Double Bogey"
        else:
            return "Above Double Bogey"
       
    def calculateTotalScore(scores):
        return sum(scores)