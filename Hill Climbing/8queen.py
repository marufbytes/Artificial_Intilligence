
# ============================================================================
# EXAMPLE USAGE: 8-Queen Problem (Simplified for demonstration)
# ============================================================================
 
# Simple test function: counting conflicts (fewer is better, so we negate)
def simple_test_evaluate(state):
    """
    Simple test evaluation function
    state is a list of numbers
    Returns: sum of state (higher is better)
    """
    return sum(state)
 
 
def simple_test_neighbors(state):
    """
    Generate neighbors by changing one element by ±1
    state is a list of numbers
    """
    neighbors = []
    # Loop through each position in state
    for i in range(len(state)):
        # Create neighbor by incrementing position i
        neighbor1 = state[:i] + [state[i] + 1] + state[i+1:]
        neighbors.append(neighbor1)
        
        # Create neighbor by decrementing position i
        neighbor2 = state[:i] + [state[i] - 1] + state[i+1:]
        neighbors.append(neighbor2)
    
    return neighbors
 