# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import random

INTERVAL = [-20, 20]  # Interval
NUM_EXPERIENCE = 10000  # Number of experience
NUM_OF_TRIPS = 30  # Number of walks
INITIAL_POSITION = 0  # Starting position


def get_interval_length(interval):
    interval_dist = 0
    if interval[0] < interval[1]:
        if interval[0] < 0 and interval[1] < 0:
            interval_dist += abs(interval[0] - interval[1])
        elif interval[0] < 0 and interval[1] > 0:
            interval_dist += abs(interval[0]) + interval[1] + 1
        elif interval[0] >= 0 and interval[1] > 0:
            interval_dist += interval[1] - interval[0]

    return interval_dist


def generate_random_prob(interval):
    interval_length = get_interval_length(interval)
    generated_probabilities = np.zeros((interval_length, interval_length), np.float)
    for i in range(interval_length):
        if i == 0:
            generated_probabilities[i, i + 1] = 1
        elif i == interval_length - 1:
            generated_probabilities[i, i - 1] = 1
        else:
            prob_to_go_right = random.random()
            generated_probabilities[i, i + 1] = prob_to_go_right
            generated_probabilities[i, i - 1] = 1 - prob_to_go_right

    return generated_probabilities


def walk_simulation(initial_pos, interval, num_of_walks, probs):
    prob_index = 0
    while interval[0] != initial_pos:
        interval[0] += 1
        prob_index += 1

    position = initial_pos
    for i in range(num_of_walks):
        if prob_index == interval[0]:
            position += 1
            prob_index += 1
        if prob_index == interval[1]:
            position -= 1
            prob_index -= 1
        else:
            is_moving_right = random.random() < probs[prob_index, prob_index + 1]
            if is_moving_right:
                position += 1
                prob_index += 1
            else:
                position -= 1
                prob_index -= 1

    return position


if __name__ == '__main__':
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    probabilities = generate_random_prob(INTERVAL)
    final_positions = []
    for i in range(NUM_EXPERIENCE):
        walk = walk_simulation(INITIAL_POSITION, INTERVAL, NUM_OF_TRIPS, probabilities)
        axes[0].scatter(walk, 0)
        final_positions.append(walk)

    print(final_positions)

    # Show raw result
    axes[0].grid(True)
    axes[0].set_title('Résultat des positions obtenues')
    axes[0].spines['left'].set_position('zero')
    axes[0].spines['right'].set_color('none')
    axes[0].spines['bottom'].set_position('zero')
    axes[0].spines['top'].set_color('none')

    # Show histogram
    axes[1].hist(final_positions, bins=16)
    axes[1].set_title('Positions finales')

    fig.tight_layout()
    plt.show()
