# create a list of tuples from given list having number and its cube in each tuple
# using ** operator method
list = [4,2,3,5,7]
result = [(value, value**3) for value in list]
print(result)
