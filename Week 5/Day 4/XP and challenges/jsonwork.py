import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_file = 'pract.json'

with open(json_file, 'r') as file_obj:
    sampleJson = json.load(file_obj)

print (sampleJson)
# my_family = {
#     "parents":['Beth', 'Jerry'],
#     "children":['Summer', 'Morty']
# }


# with open(json_file, 'w') as file_obj:
#     json.dump(my_family, file_obj, indent=4, sort_keys=True)

# with open(json_file, 'r') as file_obj:
#     my_family = json.load(file_obj)

# print(my_family)
# json.load('json.json')


