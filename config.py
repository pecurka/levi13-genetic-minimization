import math

repetitions = 5
max_iter = 500
mut_rate = 0.2
alpha = 0.5
pop_size = 100
scope = [-10, 10]
selection_size = 4
round_value = 10

def fitness_function(x, y):
    return math.pow(math.sin(3*math.pi*x), 2) + math.pow(x - 1, 2)*(1 + math.pow(math.sin(3*math.pi*y), 2)) + math.pow(y - 1, 2)*(1 + math.pow(math.sin(2*math.pi*y), 2))
