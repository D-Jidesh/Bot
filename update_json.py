import json

person_dict =dict()
print("Enter destination name: ")
name=input()
name=name.replace(" ","_")
print("Enter destination location: ")
loc=input()
person_dict[name]=loc
print(person_dict)

with open('labs.json', 'a+') as json_file:
  json.dump(person_dict, json_file)
  json_file.write('\n')
