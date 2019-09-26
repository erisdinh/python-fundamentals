# Tuple exercises
# create tuples

t = (1, 'python', [2,3], (4,5))

# Unpack t into 6 variables
a,b,c,e = t
c,d = c
e, f = e

print("Unpack tuple t: ", a,b,c,d,e,f)

# print last element of tuple t
print("Last element of tuple t: ", t[len(t) -1])


#Add to t a list [2,3]
l = ([2,3],)
t = t + l
print("Tuple t after adding list [2,3]: ", t)

#Check wheter list [2,3] is duplicated in t
isDuplicated = False
count = t.count([2,3])
if count > 1:
    isDuplicated = True

print("Check list [2,3] is duplicated in t: ", isDuplicated)

print(t)
#Remove list [2,3] from t
tempList = list(t)
subList = [2, 3]

i = 0
while i < len(tempList):
    if tempList[i] == subList:
        del tempList[i]
    i = i +1

t = tuple(tempList)
print("After removing list [2, 3] from t: ", t)

#Convert t into a list
t = list(t)
print("t after converting into a list: ", t)
print("Type of t: ", type(t))

