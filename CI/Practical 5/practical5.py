import numpy as np

# Define problem-specific parameters
POP_SIZE = 10      # Number of antibodies (candidate solutions)
CLONE_FACTOR = 3   # Number of clones per selected antibody
MUTATION_RATE = 0.2 # Probability of mutation
ITERATIONS = 50    # Maximum number of iterations

# Define fitness function (Affinity Function)
def fitness_function(x):
    return -np.sum((x - 0.5) ** 2)  # Example: minimizing squared distance from 0.5

# Initialize population (random real-valued antibodies)
def initialize_population(size, dim=5):
    return np.random.rand(size, dim)

# Select top antibodies based on fitness
def select_best(population, fitness, num_selected):
    indices = np.argsort(fitness)[-num_selected:]  # Select highest fitness
    return population[indices], fitness[indices]

# Clone selected antibodies
def clone_population(selected, clone_factor):
    clones = np.repeat(selected, clone_factor, axis=0)
    return clones

# Introduce mutations (hypermutation)
def mutate_population(clones, mutation_rate):
    mutations = (np.random.rand(*clones.shape) < mutation_rate) * np.random.uniform(-0.1, 0.1, clones.shape)
    return np.clip(clones + mutations, 0, 1)  # Ensure values remain in [0,1]

# Main CLONALG algorithm
def clonal_selection_algorithm():
    population = initialize_population(POP_SIZE)
    
    for iteration in range(ITERATIONS):
        fitness = np.array([fitness_function(ind) for ind in population])
        selected, selected_fitness = select_best(population, fitness, POP_SIZE // 2)
        clones = clone_population(selected, CLONE_FACTOR)
        mutated_clones = mutate_population(clones, MUTATION_RATE)
        
        # Evaluate fitness of new population (mutated clones + original population)
        new_population = np.vstack((population, mutated_clones))
        new_fitness = np.array([fitness_function(ind) for ind in new_population])
        
        # Select best individuals for the next generation
        population, _ = select_best(new_population, new_fitness, POP_SIZE)
        
        best_fitness = max(new_fitness)
        print(f"Iteration {iteration + 1}: Best Fitness = {best_fitness:.5f}")
    
    # Return the best solution found
    best_solution = population[np.argmax([fitness_function(ind) for ind in population])]
    return best_solution

# Run the Clonal Selection Algorithm
best_solution = clonal_selection_algorithm()
print("Best Solution Found:", best_solution)
