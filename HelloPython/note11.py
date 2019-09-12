# Tuples
# tuples can not be changed
numbers = (1, 2, 3)

# Unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates
print(f'{x}, {y}, {z}')

# Dictionaries
customer = {"name": "xuan",
            "age": 25,
            "is_rich": False}
print(customer["name"])
# if the key is not exiting, return "none"
print(customer.get("add"))
# get the default value
print(customer.get("address", "st"))
# adding key value
customer["birthday"] = "1993"
print(customer["birthday"])





