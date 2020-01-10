import random as r
class Mutation:
    def __init__(self, job_client, client_fe_lifecyle):
        self.job_client = job_client
        self.client_fe_lifecyle = client_fe_lifecyle


    def controlled_mutation(self, ind):
        solution = ind.copy()
        mutation_point = r.randint(0, len(solution)-1)
        client = self.job_client[mutation_point]
        possible_fes_temp = list(self.client_fe_lifecyle[client].keys())
        current_fe = solution[mutation_point]
        possible_fes_temp.remove(current_fe)
        solution[mutation_point] = r.choice(possible_fes_temp)
        return solution.copy()

