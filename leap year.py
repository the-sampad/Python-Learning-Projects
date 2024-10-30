# First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year."
# it should return True if it is a leap year and return False if it is not a leap year.

# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

# days_in_month(year=2022, month=2)
 
# And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

# 28

# The List month_days contains the number of days in a month from January to December for a non-leap year. 

# A leap year has 29 days in February.




from calendar import month_name


def is_leap(year):
    if year%4==0:
        if year%400==0:
            return True
        elif year%100!=0:
            return True
    else:
        return False

def days_in_month(year,month):
    leap = is_leap(year)
    month_list = list(month_name)
    month_num = month_list.index(month)
    if leap==True and month_num==2:
        return 29
    elif leap==False and month_num==2:
        return 28
    elif month_num in [1,3,5,7,8,10,12]:
        return 31
    elif month_num in [4,6,9,11]:
        return 30
i=1
while i:
    year = int(input('Enter the year : '))
    month = input('Enter the month name : ').title()
    if is_leap(year)==True:
        leap = 'It is Leap Year'
    else:
        leap = ''

    print(f'No. of days in the month is {days_in_month(year,month)}. {leap}')

    b = input('Do you want to test for another combination ? Yes or No').lower()
    if b=='yes':
        i=i
    elif b=='no':
        i-=1
    else:
        print('Invalid Input')
