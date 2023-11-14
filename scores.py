scores = []

def addScore(s):
    scores.append(s)

def getScore():
    return scores

def getTotalScore():
    total = 0
    for score in scores:
        total += score
    return total

def getAvgScore():
    avg = getTotalScore() / len(scores)
    return avg