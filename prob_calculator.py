import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.content = []
        if not kwargs:  # Error check
            print ("No balls in hat.")
            return
        for colour, amount in kwargs.items():  # Build hat.contents
            for count in range(0, amount):
                self.content.append(colour)

    def draw (self, num_balls_to_draw):
        balls_to_return = []
        if num_balls_to_draw >= len(self.content):
            balls_to_return = self.content[:]  # Copy across all hat contents (could also use copy.copy here)
            self.content = []  # Empty contents of hat
        else:
            balls_to_return = []  # This will be our output string
            for count in range(0,num_balls_to_draw):
                num_balls_in_hat = len(self.content) - 1  # How many balls are currently in the hat
                ball_to_draw = random.randint(0, num_balls_in_hat)  # Get our random ball
                removed_ball = self.content.pop(ball_to_draw) # Remove ball from hat
                balls_to_return.append(removed_ball)
        return balls_to_return

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    all_balls_found = 0
    for count in range(0, num_experiments):
        this_hat = copy.deepcopy(hat)
        found = []
        for loop in range(0, len(expected_balls)):  # For each expected ball type set flag indicating not found
            found.append("False")
        balls_drawn_this_iter = this_hat.draw(num_balls_drawn)  # Draw balls from hat
        found_count = 0
        for colour, amount in expected_balls.items():  # Iterate through the colour and amount of expected balls
            amount_drawn = balls_drawn_this_iter.count(colour)  # The number of expected coloured balls in this draw
            if amount_drawn >= amount:
                found[found_count] = "True"  # We have found our balls in this draw (yes I could word this better)
            found_count += 1
        if all(flag == "True" for (flag) in found):
            all_balls_found += 1
            
    # Calculate probability
    probability = all_balls_found / num_experiments
    return float(probability)

