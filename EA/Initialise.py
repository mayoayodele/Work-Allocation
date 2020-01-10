import pandas as pd
from Solution import * 
import random
import numpy as np
import json


class Initialise:
    def __init__(self):
        with open('./Data/job_client.txt') as json_file:
            job_client = json.load(json_file)
        self.job_client = {int(k):int(v) for k,v in job_client.items()}
        print(self.job_client)

        self.client_fe_lifecyle = {}
        with open('./Data/client_fe_lifecyle.txt') as json_file:
            client_fe_lifecyle = json.load(json_file)
        for client in client_fe_lifecyle.keys():
            fe_lifecyles = {int(k):int(v) for k,v in client_fe_lifecyle[client].items()}
            self.client_fe_lifecyle[int(client)] = fe_lifecyles
        print(self.client_fe_lifecyle)

        with open('./Data/fe_capacity.txt') as json_file:
            fe_capacity = json.load(json_file)
        self.fe_capacity = {int(k):int(v) for k,v in fe_capacity.items()}
        print(self.fe_capacity)

        with open('./Data/fe_schedule.txt') as json_file:
            availabilities = json.load(json_file)

        self.availabilities = {}
        for fe in availabilities.keys():
            availability = {int(k):int(v) for k,v in availabilities[fe].items()}
            self.availabilities[int(fe)] = availability
        print(self.availabilities)
        
    
    
    def get_random_solution(self):
        solution = Solution()
        ind = []
        lifecycle = []
        for i in range(len(self.job_client)):
            possible_fes = list(self.client_fe_lifecyle[self.job_client[i]].keys())
            fe = random.choice(possible_fes)
            ind.append(fe)

        solution.set_ind(ind)
        solution.set_lifecyles(self.estimate_lifecycles(ind))
        solution.set_capacities(self.get_capacities(ind))
        solution.set_availabilities(self.get_availabilities(ind))
        solution.set_fitness()
        return solution


    def estimate_lifecycles(self, ind):
        ind_lifecycles = {}
        for i in range(len(ind)):
            temp_lifecycle = self.client_fe_lifecyle[self.job_client[i]][ind[i]]
            ind_lifecycles[i] = temp_lifecycle
        return ind_lifecycles
        

    def get_capacities(self, ind):
        capacity = {}
        for i in ind:
            capacity_level = self.fe_capacity[i]
            capacity[i] = capacity_level
        return capacity


    def get_availabilities(self, ind):
        availability = {}
        for i in ind:
            availability[i] = self.availabilities[i]
        return availability

    
