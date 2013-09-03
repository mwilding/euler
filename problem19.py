
SUN = 0
MON = 1
TUE = 2
WED = 3
THU = 4
FRI = 5
SAT = 6

JAN = 0
FEB = 1
MAR = 2
APR = 3
MAY = 4
JUN = 5
JUL = 6
AUG = 7
SEP = 8
OCT = 9
NOV = 10
DEC = 11

def is_sunday(day):
    """Returns true if a day is a sunday"""
    return day % 7 == SUN

def is_leap_year(year):
    """Returns true if the given year is a leap year"""

    century = year % 100 == 0
    divisible_by_400 = year % 400 == 0
    divisible_by_4 = year % 4 == 0
    if (not divisible_by_4) or (century and not divisible_by_400):
        return False
    else:
        return True

def days_in_month(year, month):
    """Returns the number of days in a given month in a given year"""

    if month == FEB:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month == SEP or \
         month == APR or \
         month == JUN or \
         month == NOV:
        return 30
    else:
        return 31


def days_in_year(year):
    """Returns the number of days in a year"""

    if is_leap_year(year):
        return 366
    else:
        return 365

def sundays_on_first_of_month(start_year, end_year, start_day):
    day = start_day
    sundays = 0
    for year in xrange(start_year, end_year + 1):
        for month in xrange(JAN, DEC + 1):
            day += days_in_month(year, month)
            if is_sunday(day):
                sundays += 1
    return sundays
