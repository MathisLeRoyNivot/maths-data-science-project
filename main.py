# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import random

INTERVAL = [-10, 10]  # Interval
NUM_EXPERIENCE = 50000  # Number of experience
NUM_OF_TRIPS = 30  # Number of walks
INITIAL_POSITION = 0  # Starting position


def get_interval_length(interval):
    interval_dist = []
    if interval[0] < interval[1]:
        for i in range(interval[0], interval[1] + 1):
            interval_dist.append(i)

    return len(interval_dist)


def generate_random_prob(interval):
    interval_length = get_interval_length(interval)
    generated_probabilities = np.zeros((interval_length, interval_length), np.float)
    for i in range(interval_length):
        if i == 0:
            generated_probabilities[i, i + 1] = 1
        elif i == interval_length - 1:
            generated_probabilities[i, i - 1] = 1
        else:
            prob_to_go_right = 0.5 + random.uniform(0.0, 0.1)
            generated_probabilities[i, i + 1] = prob_to_go_right
            generated_probabilities[i, i - 1] = 1 - prob_to_go_right

    return generated_probabilities


def walk_simulation(initial_pos, interval, num_of_walks, probs):
    prob_index = get_interval_length([interval[0], initial_pos]) - 1
    position = initial_pos

    for i in range(num_of_walks):
        if prob_index == 0:
            position += 1
            prob_index += 1
        elif prob_index == get_interval_length(interval) - 1:
            position -= 1
            prob_index -= 1
        else:
            is_moving_right = random.random() < probs[prob_index][prob_index + 1]
            if is_moving_right:
                position += 1
                prob_index += 1
            else:
                position -= 1
                prob_index -= 1

    return position


if __name__ == '__main__':
    probabilities = generate_random_prob(INTERVAL)
    final_positions = []
    for i in range(NUM_EXPERIENCE):
        walk = walk_simulation(INITIAL_POSITION, INTERVAL, NUM_OF_TRIPS, probabilities)
        final_positions.append(walk)

    # Show histogram
    plt.hist(final_positions, bins=10)
    plt.show()
