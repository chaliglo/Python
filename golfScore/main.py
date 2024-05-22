from GolfCourse import GolfCourse
from Golfer import Golfer
from Hole import Hole

# Got help from ChatGPT
def readfile(filename):
    courses = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if parts[0] == 'C':
                course = GolfCourse(parts[1], int(parts[2]), int(parts[3]))
                courses.append(course)
            elif parts[0] == 'H':
                hole = Hole(int(parts[1]), parts[2], int(parts[3]))
                course.lListofHoles.append(hole)
    return courses

def golfCourseTracker():
    filename = 'GolfCourses.txt'
    courses = readfile(filename)
    player = input("Enter the golfer's name: ")
    golfer = Golfer(player)
    courseName = courses[0]
    
    # All "if '' is not None" help was from https://rollbar.com/blog/python-typeerror-nonetype-object-is-not-iterable/
    if courses is not None:
        # Got help from ChatGPT
        for i, course in enumerate(courses, start=1):
            print(f"\n Course Name: {course.sLocation} \n\t Course Par: {course.nCoursePar} \n\t Hole Count: {course.nHoleCount} \n")
    
    if courseName is not None:
        # Got help from ChatGPT
        for hole in courseName.lListofHoles:
            score = int(input(f"What is {player}'s score for {hole.nName} (Par {hole.nPar}): "))
            golfer.lScore.append(score)
   
    if golfer is not None:
        # Got help from ChatGPT
        totalScore = Golfer.calculateTotalScore(golfer.lScore)
        print(f"\n{player}" + "\n" + f"Total Course Score: {totalScore} \n")
    
    if courseName is not None:
        # Got help from ChatGPT
        for i, (hole, score) in enumerate(zip(courseName.lListofHoles, golfer.lScore), start=1):
            category = Golfer.ScoreType(score, hole.nPar)
            print(f"Hole {i} - Par {hole.nPar}.  Score: {score} ({category})")

golfCourseTracker()

