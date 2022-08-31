import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**items):
        self.contents = list()
        for k, v in items.items():
            for i in range(v):
                self.contents.append(k)

    # Getting a random number of hats
    def draw(self,qtd):
        drawList = list()
        if qtd >= len(self.contents):
            return self.contents
        for i in range(qtd):
            balls = self.contents.pop(random.randrange(len(self.contents)))
            drawList.append(balls)
        
        return drawList

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter = 0
    for i in range(num_experiments):
        deepcopyhat = copy.deepcopy(hat)
        ballDraw = deepcopyhat.draw(num_balls_drawn)
        ballReq = 0
        for k, v in expected_balls.items():
            if ballDraw.count(k) >= v:
                ballReq += 1
        if ballReq == len(expected_balls):
            counter += 1
        
    return counter/num_experiments
                
        