def isIn(x, y):
    if (0 <= x < 5) and (0 <= y < 5):
        return True
    else:
        return False

class Checker:
    def __init__(self, place):
        self.place = place
        self.dx1 = [-1, 0, 1, 0]
        self.dy1 = [0, 1, 0, -1]
        self.dx2 = [1, 1, -1, -1]
        self.dy2 = [1, -1, 1, -1]

    def distance1_caution(self, x, y):
        for i in range(4):
            x_ = x + self.dx1[i]
            y_ = y + self.dy1[i]

            if isIn(x_, y_):
                if self.place[x_][y_] == 'P':
                    return True

                elif self.place[x_][y_] == 'O':
                    x__ = x_ + self.dx1[i]
                    y__ = y_ + self.dy1[i]

                    if isIn(x__, y__):
                        if self.place[x__][y__] == 'P':
                            return True

        else:
            return False

    def distance2_caution(self, x, y):
        for i in range(4):
            x_ = x + self.dx2[i]
            y_ = y + self.dy2[i]

            if isIn(x_, y_):
                if self.place[x_][y_] == 'P':
                    if self.place[x][y_] != 'X' or self.place[x_][y] != 'X':
                        return True

        else:
            return False


def solution(places):
    answer = []

    for place in places:
        isCaught = False
        check = Checker(place=place)

        for x in range(5):
            if isCaught:
                break

            for y in range(5):
                if place[x][y] != 'P':
                    continue

                if check.distance1_caution(x, y) or check.distance2_caution(x, y):
                    isCaught = True
                    break

        if isCaught:
            answer.append(0)
        else:
            answer.append(1)

    return answer
