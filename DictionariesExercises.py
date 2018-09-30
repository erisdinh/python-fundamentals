import operator

# Dictionary Exercises

#3.1
# Define dictionaries
from builtins import print, list

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

# Concatnate 3 dictionaries into a new one
dic = dict(dic1)
dic.update(dic2)
dic.update(dic3)
print("New combined dictionary: ", dic)

squareDic = {}
for key in range(1, 16):
    squareDic.update({key:key**2})

print("A dictionary that has the key are numbers "
      "between 1 and 15 and the values are "
      "square of the keys: \n", squareDic)

#3.2
inputDic = {'a':1, 'b':4, 'c':2}

sortedDic = dict(sorted(inputDic.items(), key=operator.itemgetter(1)))

keyList = sortedDic.keys()
print("A list of key where "
      "the order are the order of the mapped values: ", keyList)

print()
#3.3
string = "Python is an easy language to learn"

setString = set(string)
listKeyString = list(setString)

countDic = dict.fromkeys(listKeyString, 0)

for i in countDic.keys():
    for n in string:
        if n == i:
            countDic[i] = countDic[i]+1

print("Character-count Dictrionary: \n", countDic)
