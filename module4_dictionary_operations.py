# Dictionaries are mutable
# Create an empty dictionary by using CURLY brackets{}
grades = {}

# add a new element with square brackets []



grades['Anne'] = 'A'
print(grades)

# use .update to change grades as well
grades.update({'John':'A'})
print(grades)

# use len function to count the number of KEY:Value pairs
len(grades)

# in operator
if 'John' in grades:
    print('John got:', grades['John'])

del grades['John']
print(grades)

grades['John'] = 'A'
print(grades)

for el in grades:
    print(el)

for el in grades.keys():
    print(el)


grades['Anne'] = 'A'
grades['John'] = 'B'
print(grades)

for el in grades.values():
    print(el)

    for person, grade in grades.items():
        print(person, 'got', grade)


print(grades)


grades = {}
grades['John'] = 'A' 
grades['Anne'] = 'B'

el = any
for el in grades:
    print(el)