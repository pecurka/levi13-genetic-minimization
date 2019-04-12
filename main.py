import random
import sys
from config import \
    fitness_function, \
    max_iter, \
    mut_rate, \
    repetitions, \
    alpha, \
    pop_size, \
    scope, \
    selection_size, \
    round_value

# for our fitness function we are using the function we are trying to minimize
def fitness_function_value(chromosome):
    return round(fitness_function(chromosome[0], chromosome[1]), round_value)

# uniform mutation
def mutate(chromosome, rate, scope):
    if random.random() < rate:
        for i in range(len(chromosome)):
            chromosome[i] = random.uniform(*scope)
    return chromosome

# tournament selection
def selection(population, size):
    competition_list = []
    #selecting the chromosomes to compete in the tournament
    while len(competition_list) < size:
        competition_list.append(random.choice(population))
    best_chromosome = None
    best_function_value = None
    #finding the best chromosome from our list of selected ones by using the fitness function
    for selected in competition_list:
        selected_value = fitness_function_value(selected)
        if best_chromosome is None or selected_value < best_function_value:
           best_function_value = selected_value
           best_chromosome = selected
    return best_chromosome

# BLX-alpha algorithm for chromosome crossover
def crossover(chrom1, chrom2):
    new_chromosomes = [[], []]
    for i in range(2):
        for j in range(2):
            d = abs(chrom1[j]-chrom2[j])
            new_chromosomes[i].append(random.uniform(min(chrom1[j], chrom2[j])-alpha*d, max(chrom1[j], chrom2[j])+alpha*d))
    return new_chromosomes

def genetic_algorithm():
    npop_size = pop_size

    outfile = sys.stdout

    print('Algorithm started...', file=outfile)
    for k in range(repetitions):
        best_chromosome = None
        best_fitness_value = None
        iter = 0

        # initial population generation
        pop = [[random.uniform(*scope) for i in range(2)] for j in range(pop_size)]

        # generate a new generation either until we reach the maximum number of iterations or our fitness function becomes 0
        while best_fitness_value != 0 and iter < max_iter:
            new_pop = pop[:]

            while len(new_pop) < pop_size + npop_size:
                chrom1 = selection(pop, selection_size)
                chrom2 = selection(pop, selection_size)
                chrom3, chrom4 = crossover(chrom1, chrom2)
                mutate(chrom3, mut_rate, scope)
                mutate(chrom4, mut_rate, scope)
                new_pop.append(chrom3)
                new_pop.append(chrom4)

            # sort chromosomes by fitness and leave the top half for the next generation
            pop = sorted(new_pop, key=lambda chrom : fitness_function_value(chrom))[:pop_size]
            # check fitness of the current best chromosome and save if needed
            fit_val = fitness_function_value(pop[0])
            if best_fitness_value is None or best_fitness_value > fit_val:
                best_fitness_value = fit_val
                best_chromosome = pop[0]

            # find average
            generation_average_fitness = round(sum(map(fitness_function_value, pop)) / pop_size, round_value)
            print('Generation {}: best chromosome fitness: {} | average fitness: {}'.format(iter, fit_val, generation_average_fitness), file=outfile)
            iter += 1

        print('Algorithm finished in {} generations.'.format(iter))
        print('Best chromosome: ', [round(best_chromosome[0], 2), round(best_chromosome[1], 2)])

genetic_algorithm()
