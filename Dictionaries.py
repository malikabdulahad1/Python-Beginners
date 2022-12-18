# Dictionaries are the maps(which we use in flutter/Dart).

customer = {
    "name" : "Abdul Ahad",
    "age" : 30,
    "is_verified": True
}

print(customer["name"])
print(customer.get("name"))
print(customer.get('education'))

# we add defualt value instead of none

print(customer.get('ahad', '....?'))

customer['name']= 'Hasan Ali'

print(customer['name'])

customer['Birthday'] = '12 jun 2000'

print(customer['Birthday'])

