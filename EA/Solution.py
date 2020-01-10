import copy

class Solution:
    def __init__(self):
        self.ind = []
        self.lifecyles = {}
        self.capacities = {}
        self.availabilities = {}
        self.fitness = None

    def set_ind(self, ind):
        self.ind = ind.copy()

    def set_lifecyles(self, lifecyles):
        self.lifecyles = copy.deepcopy(lifecyles)
    
    def set_capacities(self, capacities):
        self.capacities = copy.deepcopy(capacities)
    
    def set_availabilities(self, availabilities):
        self.availabilities = copy.deepcopy(availabilities)


    def set_fitness(self):
        finish_times = []
        for i in range(len(self.ind)):
            availability = self.availabilities[self.ind[i]]
            capacity = self.capacities[self.ind[i]]
            maximum_job_id = max(availability.keys())
            if(len(availability) < int(capacity)):
                finish_times.append(self.lifecyles[i])
            else:
                minimum_finish_time = min(availability.values())
                finish_times.append(minimum_finish_time + self.lifecyles[1])
            availability[maximum_job_id + 1] = finish_times[i]
            self.availabilities[self.ind[i]] = availability
        self.fitness = max(finish_times)



      