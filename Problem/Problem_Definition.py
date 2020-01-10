from Parameters import * 
import random as r

class Problem_Definition:

    def __init__(self):
        self.job_client = {}
        self.client_fe_lifecyle = {}
        self.fe_capacity = {}
        self.schedule = {}
        self.fe_indices = list(range(Parameters.number_of_fe))


    def generate_client_jobs(self):
        jobs = []
        fes = []
        lifecycles = []
        capacities = []
        for i in range(Parameters.number_of_client):
            jobs.append(r.randint(Parameters.min_jobs_per_client_per_day,Parameters.max_jobs_per_client_per_day))
            fes.append(r.randint(Parameters.min_fe_per_client,Parameters.max_fe_per_client))
        
        for i in self.fe_indices:
            lifecycles.append(r.randint(Parameters.min_lifecycle,Parameters.max_lifecycle))
            capacities.append(r.randint(Parameters.min_capacity_per_fe,Parameters.max_capacity_per_fe))

        jobs = sorted(jobs)
        fes = sorted(fes)
        lifecycles = sorted(lifecycles)
        capacities = sorted(capacities)

        for j in self.fe_indices:
            self.fe_capacity[j] = capacities[j] 

        


        job_index = 0
        
        for i in range(Parameters.number_of_client):
            fes_lifecyles = {}
            fe_indices_temp = self.fe_indices.copy()
            #set job id  and corresponding client id
            for j in range(jobs[i]):
                self.job_client[job_index] = i
                job_index = job_index + 1
            #set lifecyles by client id and fe id
            for j in range(fes[i]):
                fe_index= r.choice(fe_indices_temp)
                fe_indices_temp.remove(fe_index)
                temp_lifecycle = r.randint(Parameters.min_lifecycle,lifecycles[fe_index])
                fes_lifecyles[fe_index] = temp_lifecycle
            #set capacity and schedule of each fe id
            for j in self.fe_indices:
                temp_capacity = self.fe_capacity[j]
                temp_utilisation = r.randint(1, temp_capacity)
                temp_schedule = {}
                for k in range(temp_utilisation):
                    rand = r.randrange(1,temp_lifecycle)
                    temp_schedule[k] = rand
                self.schedule[j] = temp_schedule
            self.client_fe_lifecyle[i] = fes_lifecyles
            

    


