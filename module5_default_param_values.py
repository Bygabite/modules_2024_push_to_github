print('hello', 'how are you?', end='.', sep='-')
# in PRINT function the END argument has the default value of a newline character, 
# Sep argument has default value of wide space character

def print_letter_count(text ='This is the default string to search', letter ='a'):
    counter = 0
    for char in text:
        if char == letter:
           counter += 1
           print('Number of', letter 'is', counter)

print_letter_counte('How many letters a are here?')
print_letter_count()
print_letter_count('Search here', letter='a')

