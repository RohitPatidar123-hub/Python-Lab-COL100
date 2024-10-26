import json

# with open('states.json') as f:      #open file 
#   data = json.load(f)               


# # print("Data type of type(data)",type(data)) 
# # print(data)   

# # print("Data type of type(data['states'])",type(data['states']))
# # print(data['states'])

# for person in data['states'] :
#    # print("Using for loop")
#     print(person['name'],"   ",type(person['name']))
#    # del person["abbreviation"]

# new_string =json.dumps(data ,indent =3,sort_keys=True)
# print(data) 

# print(new_string)

with open('states.json') as f:
    data =json.load(f)         # from json to data 
print("print complete file :")
for state in data['states']:
    print(state)

print("Print name and abbrevation :")

for state in data['states']:
    print(state['name'],"  ",state['abbreviation'])

for person in data['states'] :
    del person["abbreviation"]

print("Data after delete abbrevation :",data) 

with open('new.jason','w') as n :
    json.dump(data,n,indent=2)





       