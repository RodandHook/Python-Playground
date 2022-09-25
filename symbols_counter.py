from multiprocessing.sharedctypes import Value
import os
from pickle import NONE
import string
os.system('cls')

# try:
#     name = raw_input('Enger file:')
#     handle = open(name)
# except:
#     print ('does not work')
# _______________


# rawinput = input ("Enter a number: ")
# try:
#     ival = int(rawinput)
# except:
#     ival = -1

# if ival > 0:
#     print ("nice work")
# else:
#     print ("bad work")    
#________________

# while True:
#     line = input ('>')
#     if line == 'done':
#         break
#     print (line)
# print ('Finished text input cycle') 
#________________

# while True:
#     line = input('>')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print ('Done!')

#Finding max out of the array
# array = [1, 2, 3, 4, 8, 6, 12, 4, 20]
# i=0
# while i<(len(array)-1):
#     if array[i]>array[i+1]:
#         largest = array[i]
#     else: 
#         largest = array[i+1]
#     i+=1
# print(largest)

#Alternative version. Finding max out of the array

# largest_so_far = 0
# print ('Before: ', largest_so_far)
# for the_num in [1, 2, 3, 4, 8, 6, 12, 4, 20]:
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print(largest_so_far, the_num)
# print ('After: ', largest_so_far)

smallest = None
print ('Before: ', smallest)
for value in [1, 2, 3, 4, 8, 6, 12, 4, 20]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print (smallest, value)
print ('After: ', smallest)