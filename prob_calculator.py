import copy
import random
# Consider using the modules imported above.

class Hat():
    def __init__(self, **kwargs):
        '''
        Creates a contents list containing the string version of the given colors a given number of times
        '''
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
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
            return drawn_balls
        else:
            print('not enough balls')
            return False



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''
    Returns the probability of a given set of colors being picked from the original set
    '''

    print('num balls drawn', num_balls_drawn)

    guessed_right = 0
    for i in range(num_experiments):
        content_copy = copy.deepcopy(hat)
        expected_balls_copy = copy.deepcopy(expected_balls)
        # draw x amount of times
        print('drew again')
        drawn_balls = content_copy.draw(num_balls_drawn)
        if drawn_balls != False:
            # compare drawn_balls to ideal_balls. If element in drawn_balls in expected balls, remove from drawn_balls
            for color in drawn_balls:

                print(color)

                if color in expected_balls_copy:


                    print('Drawn', drawn_balls)
                    print('color', color)
                    print('ideal', expected_balls_copy)


                    expected_balls_copy[color] -= 1

                    print('ideal2', expected_balls_copy)
                else:
                    continue
        else:
            return 1.0

        if all(value < 1 for value in expected_balls_copy.values()):
            guessed_right += 1

        print('guessed', guessed_right)


    # estimate probability by number of times guess was correct / number of experiments
    probability = guessed_right / num_experiments

    print(guessed_right, num_experiments)

    return probability