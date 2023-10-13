# reverse the list
list = ['a','aa','b',3,4,5,8]
def reverse(list):
    newlist = list[ :: -1]
    return newlist

print(reverse(list))