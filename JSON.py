# import json

# data = '''
# {
#     "name" : "Chuck",
#     "phone" : {
#         "type" : "intl",
#         "number" :"+1 123 745 4569"
#     },
#     "email" : {
#         "hide" : "yes"
#     }
# }'''


# info = json.loads(data)                       .loads() converts data input into a python dictionary

# print("Name:", info['name'])
# print("Phone Number:", info['phone']['number'])
# print("Hide:", info['email']['hide'])

import json

input = '''
[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"

    },
    {
        "id" : "009",
        "x" : "7",
        "name" : "Chuck"
    }
]'''

info = json.loads(input)
print("User Count:", len(info))
print("\n")
for item in info:
    print("ID:", item["id"])
    print("Name:", item["name"])
    print("Attribute:", item['x'])
    print("------------------")