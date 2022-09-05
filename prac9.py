my_dict = {'name': 'Jaydeep', 1: [10, 11, 12], 'age':19} 
print(len(my_dict))


#accessing value
print(my_dict.get('name'))

# update value 
my_dict['age'] = 20
print(my_dict)

# add item
my_dict['address'] = 'Amravati'
print(my_dict)

#delete item
my_dict.pop(1)
print(my_dict)


# remove all items
my_dict.clear()

print(my_dict)