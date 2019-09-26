print("Hello World");

# Assign value to variables
# x = 5
# s = "welcome"
# Multi assignment
# x,y = 5, 3 -> x = 5, y = 2
# a = b = c = 1

# Can use method type() to know the type of the variable
# Ex:
# type(x); type(s)
# -> Use ; to separate the code in one line
# -> Use ; to end the line

# every character in python has an index
# ex: i am an international -> index: i -> 0, a -> 2, m -> 3
# a string -> automatically be an array
# ex: sentence = "I am an international student at Sheridan College"
#
# string[firstCharacter : lastCharacter + 1]
#
# -> sentence[3] -> Output: 'm'
# -> sentence[8:21] -> Output: 'international'
# -> sentence[:4] -> Output: 'I am'
# -> sentence[:-3] -> Output: 'I am an international student at Sheridan Coll'

# name = "Quynh"
# name += " is 22 years old"
# -> Output: 'Quynh is 22 years old'
#
# sentence = "%s is 22 years old"
# sentence%name
# -> Output: 'Quynh is 22 years old'

# sentence = "%s is 22 years old"
# sentence%("Hai")
# -> Output: 'Hai is 22 years old'

# sent = "%s %s is the President of the US"
# sent%("Barrack", "Obama")
# 'Barrack Obama is the President of the US'

# sent = "%s is %d years old"
# sent%("Quynh", 22)
# -> Output: 'Quynh is 22 years old'

# sentence = sent%("Quynh", 22)
# sentence
# -> Output: 'Quynh is 22 years old'

# LISTS
# USING SQUARE BRACKET
# Define a list
# shoplist = ["apple", "orange", "banana", "chese"] -> square bracket
# shoplist[0]
# -> Output: 'apple'

# Get a sublist from a list
# shoplist[0:2]
# -> Output: ['apple', 'orange'] -> Get the elements from index 0 to index 2-1 = 1

# Update a value into a list
# Change "apple" to "Cherry"
# shoplist[0] = "Cherry"
# shoplist
# -> Output: ['Cherry', 'orange', 'banana', 'chese']

# Delete a element in a list
# del list[index]
# Delete "orange" - index 1
# del shoplist[1]
# -> Output: ['Cherry', 'banana', 'chese']

# How many elements in a list
# len(list)
# Ex:
# len(shoplist)
# -> Output: 3

# shoplist2 = ["jam", "peanut butter", "juice"]

# Combine list to list -> Concatnate list1 and list2
# shoplist + shoplist2
# ['Cherry', 'banana', 'chese', 'jam', 'peanut butter', 'juice']

# Repeat list n times
# list * n
# Ex: shoplist * 2
# ['Cherry', 'banana', 'chese', 'Cherry', 'banana', 'chese']

# Find a max number value in a num list
# max(list)
# Ex:
# listnum = [1, 3, 4, 5, 27, 65, 33]
# max(listnum)
# -> Output: 65
# -> Otherwise, use min(list) for the minimum number

# DICTIONARIES
# USING CURLY BRACKET
# Every dictionaries has a key and a
# value

# Define a dictionary:
# dictionaryName = {key: value, key: value} -> curly bracket
# Ex:
# students = {"Bob": 12, "Rachel": 13, "Emily": 15}
# students
# -> Output: {'Bob': 12, 'Rachel': 13, 'Emily': 15}

# Retrieve a value of a key from a dictionary
# student
# dictionaryName[key]
# Ex:
# students["Bob"]
# ->Output: 12

# Update a value of a key
# dictionaryName[key] = newValue
# Ex:
# Change "Rachel" 13 to "Rachel" 23
# students["Rachel"] = 23
# students["Rachel"]
# -> Output: 23

# Remove a pair of data from a dictionary
# del dictionaryName[key]
# Ex:
# del students["Emily"]
# students
# -> Output: {'Bob': 12, 'Rachel': 23}

# Get the length of a dictionary
# len(dictionaryName)
# Ex:
# len(students)
# -> Output: 2

# ** CANNOT HAVE THE SAME KEY WITH DIFFERENT VALUES
# ** -> EVERY KEY IS UNIQUE

# TUPLES
# USING ROUND BRACKET

# Define a tuples
# tupleName = (value, value, value)
# Ex:
# tuples = ("oranges", "apples", "bananas")
# tuples
# -> Output: ('oranges', 'apples', 'bananas')
# tuples[0]
# 'oranges'

# ** CANNOT UPDATE OR CHANGE A TUPLE BY ASSIGNMENT
# ** Ex: tuples[0]
#        -> Output: 'oranges'
#        -> CANNOT: tuples[0] = 3

# Add tuples to tuples (Concatnate tuples1 and tuples2)
# tuples2 = (11, 12, 14)
# tuples3 = tuples + tuples2
# tuples3
# ('oranges', 'apples', 'bananas', 11, 12, 14)

# Remove a tuple
# del tupleName
# Ex:
# del tuples
# ** CANNOT REMOVE A SPECIFIC ITEMS (ELEMENT) FROM A TUPLE

# Get a length of tuple
# len(tupleName)
# Ex:
# len(tuples3)
# -> Output: 6

# Repeat a tuple n times
# tuplesName * n
# Ex:
# tup = ("Hi", "Hello")
# tup * 3
# -> Output: ('Hi', 'Hello', 'Hi', 'Hello', 'Hi', 'Hello')