import numpy as np
import pandas as pd
from Initialise import *
from Operators import *
from GAOperators.Selection import *
from Parameters import *
from Utils import *
import copy


results_dict = {}

init = Initialise()

population = []
for i in range(Parameters.pop_size):
    solution =init.get_random_solution() 
    population.append(solution)
    
population.sort(key=lambda x: x.fitness, reverse=False)
best_solution = population[0]
print('Generation 0')
print(best_solution.ind)
print(best_solution.fitness)
print(Utils.get_average_fitness(population))

results_dict[0] = [best_solution.ind, best_solution.fitness, Utils.get_average_fitness(population)]

selection = Selection(init)

for i in range(Parameters.number_of_generations):
    #perform selection, crossover and mutation
    offspring_population = []
    offspring_population.extend(selection.tournament_selection(population))

        

    #perform elitism of offspring and parent population
    temp_population = []
    temp_population.extend(selection.select_best_individuals(offspring_population, population[:Parameters.elitism]))

    population = []
    population.extend(temp_population)
    best_solution = population[0]
    print('Generation', i + 1)
    print(best_solution.ind)
    # print(best_solution.lifecyles)
    # print(best_solution.availabilities)
    print(best_solution.fitness)
    print(Utils.get_average_fitness(population))
    results_dict[i] = [best_solution.ind.copy(), best_solution.fitness, Utils.get_average_fitness(population)]
   


results = pd.DataFrame.from_dict(results_dict, orient='index',  columns=['Best Solution','Best Fitness', 'Average Fitness'])
results.to_excel('./results.xlsx')
    # operator = Operators(5)
    # operator.get_new_population(population)

