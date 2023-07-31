marks = [90, 95, 99, "Maths"]

print(marks[1])
# print position one

print(marks[-1])
# when we put -1 position then it's showing last in first in python

print(marks[0:2])
# print 0 and 1 position 

for score in marks:
    print(score)

# Append method add new element
marks.append(99)
print(marks)

# insert method add new element specific position
marks.insert(0, 96)
print(marks)

# exist in list or not this number
print(96 in marks)

# length of list
print(len(marks))

# using while loop how we print our list
i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

# clear whole loop
marks.clear()
print(marks)
