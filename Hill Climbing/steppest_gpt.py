# STEEPEST-ASCENT HILL CLIMBING

def objective_function(x):
    return -x**2 + 10


def get_neighbors(x, step):
    return [x - step, x + step]


def steepest_hill_climbing(start, step, max_iterations):
    current = start
    current_value = objective_function(current)

    for i in range(max_iterations):
        neighbors = get_neighbors(current, step)

        best_neighbor = current
        best_value = current_value

        # Check all neighbors
        for neighbor in neighbors:
            value = objective_function(neighbor)

            if value > best_value:
                best_neighbor = neighbor
                best_value = value

        # Stop if no improvement
        if best_neighbor == current:
            break

        current = best_neighbor
        current_value = best_value

    return current, current_value


# INPUT
start = int(input("Enter starting value: "))
step = int(input("Enter step size: "))
iterations = int(input("Enter max iterations: "))

# RUN
best_x, best_value = steepest_hill_climbing(start, step, iterations)

# OUTPUT
print("\nFinal Result (Steepest HC):")
print("Best x =", best_x)
print("Maximum value =", best_value)