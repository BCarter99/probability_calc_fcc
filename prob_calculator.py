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
        # if number of balls > len(contents) do nothing, print('Not enough balls')
        if len(self.contents) <= num_to_draw:
            drawn_balls = []
            # use copy import to make a copy of the hat in order to pull balls out w/o effecting the original hat
            content_copy = copy.deepcopy(self.contents)
            # use random import to remove a random item from the list, adding it to another list
            for i in range(num_to_draw):
                ball = random.choice(self.contents)
                drawn_balls.append(ball)
                self.contents.remove(ball)
            print(self.contents, drawn_balls)
        else:
            print('Not enough balls')


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  pass