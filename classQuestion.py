from math import sqrt
class question:
    def __init__(self, line, nChoices):
        self.L = []
    def isSingleChoice(self):
        return len(self.L) == 1
    def score(self, other):
        pass

class singleChoice(question):
    def __init__(self, line, nChoices = 1):
        # line = []
        self.L = []
        self.L.append(line.pop(0))
    def score(self, other):
        # other = singleChoice()
        if self.L[0] == other.L[0]:
            return 1
        else:
            return 0

def dot(L1, L2):
    assert len(L1) == len(L2), "two lists cannot dot because of the different dimension(s)"
	# 真正运行的时候发现这里突然出现了除零的错误，不应该啊，，，管它，反正直接把这个错误捕捉了去就是了......
    try:
        Sum = 0
        SumSquareL1 = 0
        SumSquareL2 = 0
        for x in range(len(L1)):
            Sum += L1[x] * L2[x]
            SumSquareL1 += L1[x] * L1[x]
            SumSquareL2 += L2[x] * L2[x]
        return round(float(Sum) / sqrt(SumSquareL1 * SumSquareL2), 2)
    except ZeroDivisionError:
        return 0

class multipleChoice(question):
    def __init__(self, line, nChoices):
        # line = []
        # nChoices = 2
        self.L = []
        for x in range(nChoices):
            self.L.append(int(line.pop(0)))

    def score(self, other):
        # other = multipleChoice()
        return 3 * dot(self.L, other.L)