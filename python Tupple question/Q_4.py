# Update each element in tuple list

tuple = [(6,45,'f'), (2,46,'F'), (7,56,'M')]
def update_tuple(tuple, new_val):
    for i in range(len(tuple)):
        x, y, z = tuple[i]
        tuple[i] = (new_val, y, new_val)
    return tuple
new_val = 10

updated_tuple = update_tuple(tuple, new_val)
print(updated_tuple)
