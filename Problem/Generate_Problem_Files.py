import json
from Problem_Definition import *



prob = Problem_Definition()

prob.generate_client_jobs()

print('JOB and CLIENT')
print(prob.job_client)
with open('./Data/job_client.txt', 'w') as outfile:
    json.dump(prob.job_client, outfile)


print('CLIENT, FE and LIFECYCLES')
print(prob.client_fe_lifecyle)
with open('./Data/client_fe_lifecyle.txt', 'w') as outfile:
    json.dump(prob.client_fe_lifecyle, outfile)



print('FE and CAPACITY')
print(prob.fe_capacity)
with open('./Data/fe_capacity.txt', 'w') as outfile:
    json.dump(prob.fe_capacity, outfile)


print('FE and AVAILABILITIES')
print(prob.schedule)
with open('./Data/fe_schedule.txt', 'w') as outfile:
    json.dump(prob.schedule, outfile)

