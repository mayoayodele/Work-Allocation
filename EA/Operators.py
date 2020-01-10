import random as r
class Operators:
    def __init__(self, truncation_size):
        self.truncation_size = truncation_size
        self.possible_integers = []
        
    

    def get_probabilistic_model(self, population):
        temp_population = population.copy()
        #sort solutions by fitness
        temp_population.sort(key=lambda x: x.fitness, reverse=False)
        problem_size = len(temp_population[0].ind)
        
        possible_integers = []
        new_temp_population = []
        values_per_job = {}
        model = {}


        for i in range(self.truncation_size):
            ind = temp_population[i].ind
            new_temp_population.append(ind)
            possible_integers.extend(ind)
        possible_integers = list(set(possible_integers))
        possible_integers.sort()

        print(new_temp_population)

        self.possible_integers = possible_integers.copy()

        for i in range(problem_size):
            temp = [values[i] for values in new_temp_population]
            values_per_job[i+1] = temp

        for i in values_per_job.keys():
            temp = []
            for j in possible_integers:
                try:
                   temp.append(values_per_job[i].count(j)/len(values_per_job[i]))
                except:
                    temp.append(0)
            model[i] = temp

        return(model)



    def get_new_population(self, population):
        model = self.get_probabilistic_model(population).copy()
        new_population = []
        
        for p in range(len(population)):
            solution = []
            for i in model.keys():
                rand = r.random()
                sum = 0
                probabilities = model[i]
                j = 0
                while sum < rand:
                    sum = sum + probabilities[j]
                    j=j+1
                solution.append(self.possible_integers[j-1])
            new_population.append(solution.copy())

       
        print('new population')
        print(new_population)
   
   








        # lst2 = [item[0] for item in lst]

        # for i in range(self.truncation_size):
        #     ind = temp_population[i].ind
        #     new_temp_population.append(ind)
        #     print(ind)
        #     for j in ind:
        #         if(j not in possible_integers):
        #             possible_integers.append(j)
        # possible_integers.sort()
        # print(possible_integers)
        # for i in range(len(new_temp_population)): 
        #     temp = []
        #     for j in range(possible_integers):
        #         temp


        # for solution in new_temp_population:
        #     print('Fitness sol')
        #     print(solution.fitness)
