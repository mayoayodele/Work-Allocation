import numpy as np
class Utils:

    @staticmethod
    def get_average_fitness(population):
        fitnesses = []
        for solution in population:
            fitnesses.append(solution.fitness)
        return np.mean(fitnesses)

    @staticmethod
    def are_equal(ind1, ind2):
        for i in range(len(ind1)):
            if(ind1[i] != ind2[i]):
                return False
        return True
