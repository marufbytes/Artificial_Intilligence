def steepest_ascent_hill_climbing(initial_state, get_neighbors, evaluate, max_iterations=100):
    """
    Steepest-Ascent Hill Climbing Algorithm
    - Evaluates ALL neighbors first
    - Moves to the BEST neighbor (highest value)
    - More thorough than Simple Hill Climbing
    
    Parameters:
    - initial_state: Starting position
    - get_neighbors: Function to generate neighboring states
    - evaluate: Function to evaluate state quality (higher = better)
    - max_iterations: Maximum iterations to run
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
        
        # Track the best neighbor found so far
        best_neighbor = None
        # Track the best neighbor's value
        best_neighbor_value = current_value  # Start with current value
        
        # Loop through ALL neighbors to find the best one
        for neighbor in neighbors:
            # Evaluate this neighbor's quality
            neighbor_value = evaluate(neighbor)
            
            # Check if this neighbor is better than the best found so far
            if neighbor_value > best_neighbor_value:
                # Update best neighbor
                best_neighbor = neighbor
                # Update best value
                best_neighbor_value = neighbor_value
        
        # After checking ALL neighbors, check if we found any improvement
        if best_neighbor is None:
            # No neighbor was better than current state
            # We reached a local maximum, stop here
            break
        
        # Move to the best neighbor found
        current_state = best_neighbor
        # Update current value
        current_value = best_neighbor_value
        
        # Print progress
        print(f"Steepest HC - Iteration {iteration}: State = {current_state}, Value = {current_value}")
    
    # Return the best state found and its value
    return current_state, current_value
 
 