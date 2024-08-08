# Assertions are assumptions in our program that should always be true.
def calculate_inverse(number):
    assert(number !=0), 'Got 0 as number!'
    return 1/number

calculate_inverse(0)

# USE assertions 
# 1. Debugging and testing your code
# 2. Documenting your code
