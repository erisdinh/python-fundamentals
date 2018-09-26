import math

print("Question 1: ")
u,v,x,y,z = 29, 12, 10, 4, 3

# a.
print("u/v = ", u / v)

# b.
t1 = (u==v)
print("t = ", t1)

# c.
print("u % x = ", u % x)

# d.
t2 = (x >= y)
print("t = ", t2)

# e.
u+=5
print("u += 5 => u = ", u)

# f.
u %= z
print("u %= z => u = ", u)

# g.
t3 = ( v > x and y < z)
print("t = (v > x and y < z) => t = ", t3)

# h.
print("X ** z = ", x**z)

# i.
print("x // z = ", x//z)

print()
print("Question 2:")
s = "Hi John, welcome to python programming for beginners!."

# a. check "python" in the string
check = "python" in s
print("Check \"python\" in string s: ", check)

# b. extract the word "John"
s1 = s[3:7]
print("Extract the word \"John\": ", s1)

# c. Count how many word in s
list = s.split()
print("Number of word in s: ", len(list))

print()
print("Question 3:")

r = 5;
perimeter = 2 * math.pi * r
area = math.pi * r**2

print("Perimeter of the circle: ", perimeter)
print("Area of the circle: ", area)

print()
print("Qeustion 4:")
string = "Twinkle, twinkle, little star, How I wonder what you are! " \
         "Up above the world so high, Like a diamond in the sky. " \
         "Twinkle, twinkle, little star, How I wonder what you are."
space = "      "

print(string[:30])
print(space + string[31:58])
print(string[58:84])
print(space + string[85:112])
print(string[113:144])
print(space + string[144:])

print()
print("Question 5")
I = [23, 4.3, 4.2, 31, 'python', 1, 5.3, 9, 1.7]

I.remove('python')
print("Remove 'python': ", I)

print("Sort the list by ascending: ", sorted(I))
print("Sort the ist by descending: ", sorted(I, reverse=True))

inI = 4.2 in I;
print("Check 4.2 is in I or not: ", inI)