import random as r
from GAOperators.Crossover import *
from GAOperators.Mutation import *
from Parameters import *
from Solution import *
import copy


class Selection:
    def __init__(self, init):
        self.init = init
        job_client = init.job_client
        client_fe_lifecyle = init.client_fe_lifecyle 
        self.Mutation = Mutation(job_client, client_fe_lifecyle)


  
    def tournament_selection(self, population):
        parent_population = copy.deepcopy(population)
        offspring_population = []
        for p in range(len(population)):
            parents = []
            for i in range(2):
                temp_population = []
                for j in range(Parameters.tournament_size):
                    temp_population.append(r.choice(parent_population))
                #sort solutions by fitness
                temp_population.sort(key=lambda x: x.fitness, reverse=False)
                parents.append(temp_population[0].ind.copy())
        
            
            #perform crossover
            if(r.random() < Parameters.crossover_prob): 
                if(Parameters.crossover_type==1):
                    child = Crossover.one_point_crossover(parents)
                elif(Parameters.crossover_type==2):
                    child = Crossover.two_point_crossover(parents)
                elif(Parameters.crossover_type==3):
                    child = Crossover.uniform_crossover(parents)
                else:
                    print("Invalid Crossover Type")
                    break
            else:
                child = parents[0].copy()
      

           #perform mutation
            if(r.random() < Parameters.mutation_rate):
                child = self.Mutation.controlled_mutation(child)


            #estimate solution
            solution = Solution()
 
            solution.set_ind(child.copy())
            solution.set_lifecyles(self.init.estimate_lifecycles(child))
            solution.set_capacities(self.init.get_capacities(child))
            solution.set_availabilities(self.init.get_availabilities(child))
            solution.set_fitness()

            offspring_population.append(solution)
        offspring_population.sort(key=lambda x: x.fitness, reverse=False)
        return offspring_population

    @staticmethod
    def select_best_individuals(offspring_population, parent_population):
        temp_population = []
        temp_population.extend(offspring_population)
        temp_population.extend(parent_population)
        temp_population.sort(key=lambda x: x.fitness, reverse=False)
        new_population = []
        new_population.extend(temp_population[:len(offspring_population)])
        return(new_population)










