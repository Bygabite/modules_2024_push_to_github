def get_day(user_info):
    day = int(input('What is the day of your bday? '))
    user_info.append(day)

def get_month(user_info):
    month = int(input('What is the month (1-12) of your bday? '))
    user_info.append(month)

def get_year(user_info):
    year = int(input('What is the year of your bday? '))
    user_info.append(year)

def get_user_bday(user_info):
    try:
        get_day(user_info)
        get_month(user_info)
        get_year(user_info)
        print('So your bday is', user_info)
    except ValueError:
        print('You entered incorrect data, bye!')

print('Hi, I will collect some info about your bday!')
user_info = []
get_user_bday(user_info)

# if a function that raises an exception doesnt have a tri-accept block exception is propagated to the function that called.
#There must be a tri accept block,
#multiple functions that call each other you must propogate the excdptions to the functions above.
#we can use a single try 


