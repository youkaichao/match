from classPersonalInfo import personalInfo
from classQuestion import singleChoice
from classQuestion import multipleChoice

class Person:
    def __init__(self, line):
        # line = []
        self.Info =personalInfo(line)
        self.discipline = singleChoice(line)
        self.whereToStudy = multipleChoice(line, 4)
        self.Character = singleChoice(line)
        self.sports = multipleChoice(line, 6)
        self.music = multipleChoice(line, 6)
        self.book = multipleChoice(line, 6)
        self.L = [self.discipline, self.whereToStudy, self.Character, self.sports, self.music, self.book]
        if line[0] == '1':
            self.like = True
        else:
            self.like = False

    def score(self, other):
        # other = Person([])
        Sum = 0
        for x in range(len(self.L)):
            Sum += self.L[x].score(other.L[x])
        return Sum

    def __str__(self):
        return str(self.Info)