# importing module
from pandas import *
 
# reading CSV file
path = "Recommendation_output.csv"
data = read_csv(path)
 
# converting column data to list
names = data['names'].tolist()
links = data['links'].tolist()
nsf_id = data['nsf_id'].tolist()

 
# printing list data
# print('names:', names)
# print('links:', links)
# print('nsf_id:', nsf_id)
name_id_dictionary = dict(zip(names, nsf_id))
# print(name_id_dictionary)

msg = "red blue green ' hello' pink orange 4pgp42g4jg42 ' world' violet 'black'"

print(msg.split("'")[1::2])
listmsg = msg.split("'")[1::2]
print(type(listmsg))
