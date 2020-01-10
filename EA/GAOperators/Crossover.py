import random as r


class Crossover:

    @staticmethod
    def one_point_crossover(parents):
        parent1 = parents[0]
        parent2 = parents[1]
        child = []
        gene_length = len(parent1)
        crossover_point = r.randint(1, gene_length-1)
        for i in range(gene_length):
            if i < crossover_point:
                child.append(parent1[i])
            else:
                child.append(parent2[i])

        return child.copy()

    @staticmethod
    def two_point_crossover(parents):
        parent1 = parents[0]
        parent2 = parents[1]
        child = []
        gene_length = len(parent1)
        rand1 = 0
        rand2 = 0
        while rand1 == rand2:
            rand1 = r.randint(1, gene_length-1)
            rand2 = r.randint(1, gene_length-1)

        crossover_point1 = rand1
        crossover_point2 = rand2

        if rand2 < rand1:
            crossover_point1 = rand2
            crossover_point2 = rand1

        for i in range(gene_length):
            if (i < crossover_point1) or (i >= crossover_point2):
                child.append(parent1[i])
            else:
                child.append(parent2[i])

        return child.copy()

    @staticmethod
    def uniform_crossover(parents):
        parent1 = parents[0]
        parent2 = parents[1]
        child = []
        gene_length = len(parent1)
        for i in range(gene_length):
            if(parent1[i] == parent2[i]) or (r.random() < 0.5):
                child.append(parent1[i])
            else:
                child.append(parent2[i])
        return child.copy()
