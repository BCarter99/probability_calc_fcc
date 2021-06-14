import copy
import random
# Consider using the modules imported above.

class Hat():
    def __init__(self, **kwargs):
        contents = []
        for key, value in kwargs.items():
            for color in range(value):
                contents.append(str(key))


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  pass