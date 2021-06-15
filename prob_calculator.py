import copy
import random
# Consider using the modules imported above.

class Hat():
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for color in range(value):
                self.contents.append(str(key))

    def draw(self, num_to_draw):
        '''
        Removes balls at random from contents and returns those balls as a list of strings. The balls should
        not return to the hat during the draw. If the number of balls to draw exceeds the available quantity,
        return all the balls
        '''
        drawn_balls = []
        if len(self.contents) > num_to_draw:
            # use random import to remove a random item from the list, adding it to another list
            for i in range(num_to_draw):
                ball = random.choice(self.contents)
                drawn_balls.append(ball)
                self.contents.remove(ball)
        else:
            print('Not enough balls')
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''
    Returns the probability of a given set of colors being picked from the original set
    '''
    ideal_balls = []
    # creates a list similar to self.contents, in order to compare the two
    for key, value in expected_balls.items():
        for color in range(value):
            ideal_balls.append(str(key))

    guessed_right = 0
    expected_balls_copy = copy.deepcopy(expected_balls)
    for i in range(num_experiments):
        # draw x amount of times
        drawn_balls = hat.draw(num_balls_drawn)
        # compare drawn_balls to expected balls. If element in drawn_balls in expected balls, remove from drawn_balls
        for color in range(num_balls_drawn):
            try:
                if drawn_balls[color] in expected_balls:
                    expected_balls.pop(drawn_balls[color])
                else:
                    pass
            except:
                pass
        # if expected_balls empty, +1 for how many times it was equal
        if expected_balls == []:
            guessed_right += 1
            expected_balls = expected_balls_copy
        else:
            expected_balls = expected_balls_copy
    # estimate probability by number of times guess was correct / number of experiments
    probability = guessed_right / num_experiments
    return probability