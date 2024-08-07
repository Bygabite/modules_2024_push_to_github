def show_truth():
    mysterious_var = 'Suprise!'
    print(mysterious_var)

show_truth()

# define the variable outside the function definition def():

def show_truth():
    global mysterious_var
    mysterious_var = 'New Suprise!'
    print(mysterious_var) 

mysterious_var = 'Suprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)


def show_truth():
    mysterious_var.append('New Suprise!'))
    print(mysterious_var) 

mysterious_var = 'Suprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)

