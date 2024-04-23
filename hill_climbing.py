import random
def objective_function(x):
    return -(x ** 2) 
def hill_climbing_search(bounds, n_iterations):

    solution = bounds[0] + random.random() * (bounds[1] - bounds[0])
    best = solution
    best_eval = objective_function(solution)
    
    for _ in range(n_iterations):

        candidate = solution + random.uniform(-0.1, 0.1)

        candidate_eval = objective_function(candidate)

        if candidate_eval > best_eval:
            best = candidate
            best_eval = candidate_eval
            solution = candidate
    return best, best_eval

bounds = [-10, 10]

n_iterations = 1000

best_solution, best_evaluation = hill_climbing_search(bounds, n_iterations)

print("Best Solution: x =", best_solution)
print("Best Evaluation: f(x) =", best_evaluation)
