import json


print('JOB and CLIENT')
with open('./Data/job_client.txt') as json_file:
    job_client = json.load(json_file)
print(job_client)



print('CLIENT, FE and LIFECYCLES')
with open('./Data/client_fe_lifecyle.txt') as json_file:
    client_fe_lifecyle = json.load(json_file)
print(client_fe_lifecyle)



print('FE and CAPACITY')
with open('./Data/fe_capacity.txt') as json_file:
    fe_capacity = json.load(json_file)
print(fe_capacity)


print('FE and AVAILABILITIES')
with open('./Data/availabilities.txt') as json_file:
    availabilities = json.load(json_file)
print(availabilities)

