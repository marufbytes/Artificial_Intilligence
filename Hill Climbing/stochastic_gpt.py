# STOCHASTIC HILL CLIMBING
import random

def objective_function(x):
    return -x**2 + 10


def get_neighbors(x, step):
    return [x - step, x + step]


def stochastic_hill_climbing(start, step, max_iterations):
    current = start
    current_value = objective_function(current)

    for i in range(max_iterations):
        neighbors = get_neighbors(current, step)

        # Randomly pick a neighbor
        neighbor = random.choice(neighbors)
        value = objective_function(neighbor)

        # Move only if better
        if value > current_value:
            current = neighbor
            current_value = value

    return current, current_value


# INPUT
start = int(input("Enter starting value: "))
step = int(input("Enter step size: "))
iterations = int(input("Enter max iterations: "))

# RUN
best_x, best_value = stochastic_hill_climbing(start, step, iterations)

# OUTPUT
print("\nFinal Result (Stochastic HC):")
print("Best x =", best_x)
print("Maximum value =", best_value)