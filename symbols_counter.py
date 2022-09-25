from asyncore import read
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

# smallest = None
# print ('Before: ', smallest)
# for value in [1, 2, 3, 4, 8, 6, 12, 4, 20]:
#     if smallest == None:
#         smallest = value
#     elif value < smallest:
#         smallest = value
#     print (smallest, value)
# print ('After: ', smallest)

# # Use "==" for other types
# # Use "is" on booleans and non-types, it's stronger than ==

# print ('\nYears lost: ', 2022-2004)

# # "For" loop is prefered over "while", e.g. "for letter in fruit:"

# s = "Monty Pyhon"
# print (s[0:4])

# #String Comparison
# word = input("\nPlease enter a word: ")
# if word == 'banana':
#     print ('All right, bananas')

# if word < 'banana':
#     print ('Your word, ' + word + ', comes before banana.')
# elif word > 'banana':
#     print('Your word, ' + word + ', comes after banana.')


# stuff='Hello'
# print(dir (stuff))
# print('\n\n',stuff.find('l'))

# data = 'From stephen.marquard@uct.ac.za Sat Jan   09:14:16 2008'
# atpos = data.find('@')
# print(atpos)

# sppos = data.find(' ', atpos)
# print(sppos)

# host = data[atpos+1 : sppos]
# print(host)

#               ---- READING FILES -----

# open() function doesn't open the file but it allows to open, it returns and file handle - a variable used to perform operations on the file
# handle = open(filename,mode)

fhand = open("Links.txt", 'r')
# 1. Count number of lines in the file
# print(fhand)
# count = 0
# for line in fhand:
#     count = count +1
# print('Line count: ', count)

# 2. Open lines that star with specific words
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('Git'):
#         continue
#     print(line)

# 3. Open lines that have with specific words
# for line in fhand:
#     line = line.rstrip()
#     if not 'cmd'in line:
#         continue
#     print(line)

#"print(os.getcwd())" shows the current working directory that "open" sues for as relative paths. Can be changed with os.chdir

# 4. Open specific file types in the directory
# for x in os.listdir():
#     if x.endswith(".txt"):
#         print(x)

#               ---- DATA STRUCTURES: LISTS -----

#Variables are immutable, lists are mutable
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)