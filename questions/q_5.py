# reverse the list
# list = ['a','aa','b',3,4,5,8]
# def reverse(list):
#     newlist = list[ :: -1]
#     return newlist
#
# print(reverse(list))

# **********************************************************************************
# Q_6.py
# Cloning or Copying a list
# def Cloning(list):
#     list_copy = list
#     return list_copy
# # i have to understand why do we use return---
#
# # Driver Code
# list = [4, 8, 2, 10, 15, 18]
# list2 = Cloning(list)
# print("Original List:", list)
# print("After Cloning:", list2)

# *********************************************************************************
# Q_7-
# Given a list in Python and a number 6, count the number of occurrences of x
# in the given list.

# list = [2,4,5,6,9,7,9,6,6,8,9,0,0,0,'a',6]
# # count occurences of number 6 in the list.
# def count(list,x):
#     return list.count(x)
# x=6
# print(count(list,x))
#
# # count using Pandas lib.
# import pandas as pd
# list = [2,4,5,6,9,7,9,6,6,8,9,0,0,0,'a',6]
# count = pd.Series(list).value_counts()
# print("element count")
# print(count)

# *********************************************************************

# q_8.py
# Find sum and average of List in Python

# list = [10,20,40,3,5,0,0,56,78,9,3,567]
# count = sum(list)
# avg = count/len(list)
# print("sum of the list = ", count)
# print("average of the list= ", avg)
#
# # ****************************************************************************
#
# # q_9.py
# # Multiply all numbers in the list
# import math
# list = [10,20,40,3,5]
# result = math.prod(list)
# print("multiplied result of list = ", result)
#
# # ****************************************************************************
#
# # q_10.py
# # Python program to find smallest number in a list
#
# list = [10,20,40,3,5]
# print("smallest number in the list =", min(list))
#
# # ****************************************************************************
#
# # q_11.py
# # Python Program to Find Largest Number in a List
# list = [10,20,40,3,5]
# print("largest number in the list =", max(list))
#
# # ****************************************************************************
#
# # q_12.py
# # Python program to find second largest number in a list
#
# list = [10,20,40,3,5]
# m = max(list)
# a = (a for i, a in enumerate(list) if a<m)
# print("second largest number in the list is =",max(a))
#
# # ****************************************************************************
#
# # q_13.py
# # Python program to print even numbers in a list
#
# # list = [10,20,40,3,5,0,0,56,78,9,3,567]
# #
# # for number in list:
# #     if number % 2 == 0:
# #         print(number, end= " ")
#
# # ****************************************************************************
# # q_14.py
# # # Python program to print odd numbers in a list
# # list = [10,20,40,3,5,0,0,56,78,9,3,567]
# #
# # # for number in list:
# # #     if number % 2 != 0:
# #
# #         # this is using enumeration method
# # for a, i in enumerate (list):
# #     if i % 2 != 0:
# #
# #             print(i,end= " ")
#
# # ****************************************************************************
# # q_15.py
# # Python program to print all even numbers in a range
#
# # start = int(input("Enter the start of range"))
# # end = int(input("Enter the end of range"))
# # for num in range(start, end + 1):
# #     if num % 2 == 0:
# #         print(num, end = ' ')
#
# # ****************************************************************************
# # q_16.py
# # Python program to print all odd numbers in a range
#
# a = 1
# b = 50
#
# for i in range(a, b+1 ):
#     if i%2 == 0:
#         pass
#     else:
#         print(i, end = ' ')

# ****************************************************************************
# q_17.py
# Python program to count Even and Odd numbers in a List

list = [10, 20, 40, 3, 5, 0, 0, 56, 78, 9, 3, 567]

even_count, odd_count = 0, 0
for num in list:
    if num | 1 > num:
        even_count += 1

    else:
        odd_count += 1

        print("Even numbers is list", even_count)
        print("Odd numbers in list", odd_count)


