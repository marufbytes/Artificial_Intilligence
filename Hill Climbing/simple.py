def objective_function(x):
    return -x**2 + 10


def get_neighbors(x, step):
    return [x - step, x + step]


def hill_climbing(start, step, max_iterations):
    current = start
    current_value = objective_function(current)

    for i in range(max_iterations):
        neighbors = get_neighbors(current, step)

        next_node = current
        next_value = current_value

        # Check all neighbors
        for neighbor in neighbors:
            value = objective_function(neighbor)
            if value > next_value:
                next_node = neighbor
                next_value = value

        # Stop if no improvement
        if next_node == current:
            break

        current = next_node
        current_value = next_value

    return current, current_value


start = int(input("Enter starting value: "))
step = int(input("Enter step size: "))
iterations = int(input("Enter max iterations: "))

best_x, best_value = hill_climbing(start, step, iterations)

print("\nFinal Result:")
print("Best x =", best_x)
print("Maximum value =", best_value)