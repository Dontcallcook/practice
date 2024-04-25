# Given two dictionaries, merge them into a single dictionary. 
# If a key appears in both dictionaries, add their values.

dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

dict3 = {}


for (key1, value1), (key2, value2) in zip(dict1.items(), dict2.items()):
    if key1 == key2:
        dict3[key1] = value1 + value2
    else:
        dict3[key1] = value1
        dict3[key2] = value2

print(dict3)