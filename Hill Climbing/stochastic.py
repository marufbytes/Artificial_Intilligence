 
# ============================================================================
# 3. STOCHASTIC HILL CLIMBING (Randomized Hill Climbing)
# ============================================================================
 
def stochastic_hill_climbing(initial_state, get_neighbors, evaluate, max_iterations=100, probability=0.5):
    """
    Stochastic Hill Climbing Algorithm
    - Randomly selects from BETTER neighbors (not worst ones)
    - Has probability p of accepting each better neighbor
    - Can escape local maxima more easily than deterministic versions
    
    Parameters:
    - initial_state: Starting position
    - get_neighbors: Function to generate neighboring states
    - evaluate: Function to evaluate state quality (higher = better)
    - max_iterations: Maximum iterations to run
    - probability: Probability of accepting each better neighbor (0-1)
    """
    
    # Store the current state (start from initial state)
    current_state = initial_state
    
    # Calculate the quality/fitness of current state
    current_value = evaluate(current_state)
    
    # Counter to track iterations
    iteration = 0
    
    # Main loop - continue until max iterations reached or no improvement found
    while iteration < max_iterations:
        # Increment iteration counter
        iteration += 1
        
        # Get all neighboring states
        neighbors = get_neighbors(current_state)
        
        # List to store all BETTER neighbors
        better_neighbors = []
        
        # Loop through all neighbors
        for neighbor in neighbors:
            # Evaluate this neighbor's quality
            neighbor_value = evaluate(neighbor)
            
            # Check if this neighbor is BETTER than current state
            if neighbor_value > current_value:
                # Add this better neighbor to our list
                better_neighbors.append((neighbor, neighbor_value))
        
        # Check if we found any better neighbors
        if len(better_neighbors) == 0:
            # No better neighbors exist, we're at a local maximum
            break
        
        # Randomly select one of the better neighbors
        selected_neighbor, selected_value = random.choice(better_neighbors)
        
        # Generate a random number between 0 and 1
        random_prob = random.random()
        
        # Check if we accept this neighbor based on probability
        if random_prob < probability:
            # Accept this neighbor and move to it
            current_state = selected_neighbor
            current_value = selected_value
        # If probability check fails, we stay at current state
        
        # Print progress
        print(f"Stochastic HC - Iteration {iteration}: State = {current_state}, Value = {current_value}")
    
    # Return the best state found and its value
    return current_state, current_value
 
 