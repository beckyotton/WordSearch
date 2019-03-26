# Create and print a dictionary (just print(dictionary_name)) that holds proper data for this data type.

classes_dictionary = {"physics": "p1", "comp sci": "p2", "french": "p3"}
print(classes_dictionary)

# Create a dictionary and delete any key:value pair.
'''
classes_dictionary = {"physics": "p1", "comp sci": "p2", "french": "p3"}
del classes_dictionary["comp sci"]
print(classes_dictionary)
'''

# Create an empty dictionary and add at least 3 key:value pairs to it.
'''
classes_dictionary = {}
classes_dictionary["math"] = "p1"
classes_dictionary["french"] = "p2"
classes_dictionary["science"] = "p3"
print(classes_dictionary)
'''
# Create a dictionary and algorithmically delete any key:value pair where the key starts with an “a”. (Include some keys
# that start with “a” , no loop holes plz)
delete = []
fruit_dictionary = {"apple": "red", "banana": "yellow", "apricot": "orange"}
for i in fruit_dictionary:
    if i[0] == "a":
        delete.append(i)

for i in delete:
    del fruit_dictionary[i]


print(fruit_dictionary)
