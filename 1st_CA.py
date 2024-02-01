"""1st 2mark"""
# def reverse_words(input_string):
#     words = input_string.split()
#     reversed_words = [word[::-1] for word in words]
#     reversed_string = ' '.join(reversed_words)
#     return reversed_string
# input_string = "Hello there, how are you?"
# reversed_result = reverse_words(input_string)
# print(reversed_result)
"""2nd 2mark"""
# numbers = [90,10, 20, 30, 40, 50, 60, 70, 80]
# for i in range(len(numbers) - 1, -1, -1):
#     if numbers[i] > 50:
#         del numbers[i]
# print(numbers)
"""3rd 2mark"""
# n=5
# for i in range(n, 0, -1):
#     for j in range(i, n+1):
#         print(i, end="")
#     print()
"""4th 2mark"""
# def reverse_string(input_string):
#     reversed_string = ''
#     for char in input_string:
#         reversed_string = char + reversed_string
#     return reversed_string
# input_string = input("Enter a string: ")
# reversed_result = reverse_string(input_string)
# print("Reversed string:", reversed_result)
"""5th 2mark"""
# def print_squares(x, y):
#     for num in range(x, y + 1):
#         print(f"The square of {num} is {num ** 2}")
# x = int(input("Enter the starting value: "))
# y = int(input("Enter the ending value: "))
# print_squares(x, y)
"""6th 2mark"""
# from itertools import permutations
# def print_permutations(input_string):
#     perms = permutations(input_string)
#     for perm in perms:
#         print(''.join(perm))
# input_string = input("Enter a string: ")
# print("Permutations of the string:")
# print_permutations(input_string)
"""alphabet pattern"""
# result_str="";    
# for row in range(0,7):    
#     for column in range(0,7):     
#         if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
#             result_str=result_str+"*"    
#         else:      
#             result_str=result_str+" "    
#     result_str=result_str+"\n"    
# print(result_str);
"""to get 4 digit binary number as input and return the divisible of 5"""
# bin_numbers = input("Enter a list of 4-digit binary numbers separated by comma: ").split(',')
# divisible_by_5 = []
# for bin_num in bin_numbers:
#     decimal_num = int(bin_num, 2)
#     if decimal_num % 5 == 0:
#         divisible_by_5.append(bin_num)
# print("Binary numbers divisible by 5:", divisible_by_5)
"""binary search"""
# sorted_array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# target = 10
# left, right = 0, len(sorted_array) - 1
# found = False
# while left <= right:
#     mid = left + (right - left) // 2
#     if sorted_array[mid] == target:
#         print(f"Element {target} found at index {mid}")
#         found = True
#         break
#     elif sorted_array[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# if not found:
#     print(f"Element {target} not found")
"""array concatenation"""
# import numpy as np
# array1 = np.array(["python", "php"])
# array2 = np.array(["java", "c++"])
# concatenated_array = np.core.defchararray.add(array1, array2)
# print("Concatenated array (element-wise):", concatenated_array)
'''array filtering'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
mask = arr > 3  # Create a boolean mask

filtered_arr = arr[mask]  # Apply the mask to filter the array
print(filtered_arr)  # Output: [4 5 6 7 8]










