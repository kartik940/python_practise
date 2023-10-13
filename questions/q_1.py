# # Given a list,Write Python program to swap first and last element of a list

#BEGINEER- First METHOD FOR ME
#HERE SWAPPED LIST 1 to LIST 4
# list = [2, 'd', 1, 0, 6]
# print(list[1])
# print(list[4])
# a= list[1]
# list[1],list[4]=list[4],list[1]
# list[4]=a
# print(list)

#2# (Short Method by debu)
#HERE SWAPPED LIST 2 to LIST 3
# list = [2, 'd', 1, 0, 11]
# list[2],list[3]=list[3],list[2]
# print(list)

# (Second Method BY SYSTEM) FOR BIG LIST- PREFERRED:-
# kyuki yaha p list ki length ko define ni kiya ja rha h-
# isliye jitni badi bhi size hogi usme se 1 minus hoga to automatic ho jayega

List = [12, 35, 9, 56, 24]

# Swap function
def swapList(List):
    size = len(List)

    # Swapping
    temp = List[0]
    List[0] = List[size - 1]
    List[size - 1] = temp
    return List

# Driver code
print(swapList(List))
