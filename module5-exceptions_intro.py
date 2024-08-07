# Indentation error is a type of ssyntax error
if True:
print('hooray!')

#should bring back syntax indentation error



#value error is an exception- 
# :event occurs during the execution of a program that disrupts the normal flow of the programs instructions

value = int(input('Enter an integer: '))
print('The inverse of', value, 'is', 1/value)


try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except:
    print('You did not provide a number, so I will not calculater the inverse')
#except: tells what to do after an exception is raised

# expand our code to distinguish what happens

try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except: ValueError:
    print('You did not provide a number, so I will not calculater the inverse')
except ZeroDivisionError:
    print('You provided 0 and division by 0 in not possible, sorry')
except:
    print('Something strange happened here, sorry')
