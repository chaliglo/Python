# got 'import re' with the help of ChatGPT
import re
# list to hold name and score number
nameAndScore = []
# list to hold percentage number
percent = []

# Fuction get the letter graded score
def gradedScore():
    # open text file to read
    file = open("StudentExamRecords.txt", "r")
    # get content from text file
    content = file.readlines()
    getNameAndScore()
    separateScore()
    # get size of the list
    listSize = len(percent) - 1
    assignScore(listSize)
    updateFile(listSize)
    # close text file
    file.close()

# function to get name and score from list
def getNameAndScore():
    with open("StudentExamRecords.txt", "r") as file:
        for line in file:
            nameAndScore.append(line.strip())

# function to get only the score
def separateScore():
    # separate the score from name (used ChatGPT for help)
    for item in nameAndScore:
        numbers = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", item)
        percent.extend([float(num) if '.' in num else int(num) for num in numbers])

# function to assign the letter grade
def assignScore(size):
    # loop for getting the letter grade
    counter = 0
    while counter <= size:
        if percent[counter] >= 95:
            # assign letter grade
            nameAndScore[counter] = nameAndScore[counter] + ": A\n"
            counter += 1
        elif percent[counter] < 95 and percent[counter] >= 91:
            nameAndScore[counter] = nameAndScore[counter] + ": B+\n"
            counter += 1
        elif percent[counter] < 91 and percent[counter] >= 87:
            nameAndScore[counter] = nameAndScore[counter] + ": B\n"
            counter += 1
        elif percent[counter] < 87 and percent[counter] >= 83:
            nameAndScore[counter] = nameAndScore[counter] + ": B-\n"
            counter += 1
        elif percent[counter] < 83 and percent[counter] >= 80:
            nameAndScore[counter] = nameAndScore[counter] + ": C+\n"
            counter += 1
        elif percent[counter] < 80 and percent[counter] >= 78:
            nameAndScore[counter] = nameAndScore[counter] + ": C\n"
            counter += 1
        elif percent[counter] < 78 and percent[counter] >= 75:
            nameAndScore[counter] = nameAndScore[counter] + ": C-\n"
            counter += 1
        elif percent[counter] < 75 and percent[counter] >= 70:
            nameAndScore[counter] = nameAndScore[counter] + ": D\n"
            counter += 1
        elif percent[counter] < 70:
            nameAndScore[counter] = nameAndScore[counter] + ": F\n"
            counter += 1

# function to add grade to text file
def updateFile(size):
    # loop to add grade to text file
    count = 0
    with open("StudentExamRecords.txt", "w") as file:
        while count <= size:
            file.write(str(nameAndScore[count]))
            count += 1

# Function that outputs name, grade, and letter grade
def outputResults():
    for i in range(len(nameAndScore)):
        print(nameAndScore[i])

gradedScore()
#print results
print("Grades:")
outputResults()