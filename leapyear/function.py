
def is_LeapYear(year):
    if (year%4 == 0) and (year%100 != 0):
        return True
    elif year%400 == 0:
        return True

    if (year%4 != 0):
        return False
    elif (year%100 == 0) and (year%400 != 0):
        return False
