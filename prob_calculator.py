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
            for color in range(value):
                self.contents.append(str(key))


    def draw(self, num_to_draw):
        '''
        Removes balls at random from contents and returns those balls as a list of strings. The balls should
        not return to the hat during the draw. If the number of balls to draw exceeds the available quantity,
        return all the balls
        '''
        contents_copy = copy.deepcopy(self.contents)
        drawn_balls = []
        if len(self.contents) > num_to_draw:
            # use random import to remove a random item from the list, adding it to another list
            for i in range(0, num_to_draw):
                ball = random.choice(contents_copy)
                drawn_balls.append(ball)
                contents_copy.remove(ball)
            return drawn_balls
        else:
            return self.contents



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''
    Returns the probability of a given set of colors being picked from the original set
    '''

    print('num balls drawn', num_balls_drawn)

    guessed_right = 0
    expected_balls_copy = copy.deepcopy(expected_balls)
    for i in range(num_experiments):
        # draw x amount of times
        print('drew again')
        drawn_balls = hat.draw(num_balls_drawn)
        # compare drawn_balls to ideal_balls. If element in drawn_balls in expected balls, remove from drawn_balls
        for color in drawn_balls:
            print('Drawn1', drawn_balls)

            if (color in expected_balls):


                print('Drawn', drawn_balls)
                print('color', color)
                print('ideal', expected_balls)


                expected_balls[color] -= 1

                print('ideal2', expected_balls)

        ideal_balls = []
        # creates a list similar to self.contents, in order to compare the two
        for key, value in expected_balls.items():
            for i in range(len(expected_balls)):
                if value > 0:
                    ideal_balls.append(str(key))

        # if ideal_balls empty, +1 for how many times it was equal
        if len(ideal_balls) < 1:
            guessed_right += 1

        expected_balls = expected_balls_copy
        continue


    # estimate probability by number of times guess was correct / number of experiments
    probability = guessed_right / num_experiments

    print(guessed_right, num_experiments)

    return probability