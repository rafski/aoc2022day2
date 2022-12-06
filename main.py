import numpy
import re
with open('input.txt') as f:
    games = f.read().splitlines()
    games_array = numpy.array(games)
    #print(games)
    score = 0
    for game in games_array:
        print(game)
        if re.search("A", game):
            print(score)
            if re.findall("X", game):
                score += 3 + 1
                print(score)
            if re.findall("Y", game):
                score += 6 + 2
            if re.findall("Z", game):
                score += 0 + 3
        if re.search("B", game):
            print(score)
            if re.findall("Y", game):
                score += 3 + 2
                print(score)
            if re.findall("Z", game):
                score += 6 + 3
            if re.findall("X", game):
                score += 0 + 1
        if re.search("C", game):
            print(score)
            if re.findall("Z", game):
                score += 3 + 3
                print(score)
            if re.findall("X", game):
                score += 6 + 1
            if re.findall("Y", game):
                score += 0 + 2

    print(score)

    score = 0

    for game in games_array:
        if re.search("A", game):
            if re.findall("X", game):
                score += 0 + 3
            if re.findall("Y", game):
                score += 3 + 1
            if re.findall("Z", game):
                score += 6 + 2
        if re.search("B", game):
            if re.findall("X", game):
                score += 0 + 1
            if re.findall("Y", game):
                score += 3 + 2
            if re.findall("Z", game):
                score += 6 + 3
        if re.search("C", game):
            if re.findall("X", game):
                score += 0 + 2
            if re.findall("Y", game):
                score += 3 + 3
            if re.findall("Z", game):
                score += 6 + 1

    print(score)