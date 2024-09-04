#Write a Python program to sort Python Dictionaries by Key or Value.

#Sort by keys
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

sorted_dict_by_keys = dict(sorted(sample_dict.items())) 

print("Sorted by keys:")
for key, value in sorted_dict_by_keys.items():
    print(f"{key}:{value}")


#Sort by values
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict_by_values = dict(sorted(sample_dict.items()))
print("Sorted by values:")
for key2, value2 in sorted_dict_by_values.items():
 print(f"{key2}: {value2}")